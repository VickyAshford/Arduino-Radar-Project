import pygame
import serial
import math

# --- Window settings ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
RADAR_RADIUS = 350
RADAR_CENTER_X = SCREEN_WIDTH // 2
RADAR_CENTER_Y = SCREEN_HEIGHT - 100

# --- Color settings ---
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# --- Arduino connection ---
PORT_NAME = "COM3"
BAUD_RATE = 9600

try:
    ser = serial.Serial(PORT_NAME, BAUD_RATE, timeout=1)
    print(f"Connected to {PORT_NAME}")
except Exception as e:
    print("Connection error:", e)
    ser = None

# --- Pygame setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Radar Display")
font = pygame.font.SysFont("monospace", 20)
clock = pygame.time.Clock()

# --- Data ---
current_angle = 0
current_distance = 0
point_history = []


def draw_radar_grid():
    """Draw radar grid"""
    screen.fill(BLACK)

    # Semicircles
    for i in range(1, 3):
        radius = i * (RADAR_RADIUS // 2)
        pygame.draw.arc(screen, DARK_GREEN,
                        (RADAR_CENTER_X - radius, RADAR_CENTER_Y - radius, radius * 2, radius * 2),
                        math.pi, 2 * math.pi, 2)

    # Horizontal line
    pygame.draw.line(screen, DARK_GREEN,
                     (RADAR_CENTER_X - RADAR_RADIUS, RADAR_CENTER_Y),
                     (RADAR_CENTER_X + RADAR_RADIUS, RADAR_CENTER_Y), 2)

    # Radial lines
    for i in range(5):
        angle = math.radians((i * 45) - 180)
        x2 = RADAR_CENTER_X + RADAR_RADIUS * math.cos(angle)
        y2 = RADAR_CENTER_Y + RADAR_RADIUS * math.sin(angle)
        pygame.draw.line(screen, DARK_GREEN, (RADAR_CENTER_X, RADAR_CENTER_Y), (x2, y2), 2)


def draw_text():
    """Text data"""
    angle_text = font.render(f"Angle: {current_angle} deg", True, GREEN)
    dist_text = font.render(f"Distance: {current_distance} cm", True, GREEN)
    label = font.render("Radar Display", True, GREEN)

    screen.blit(angle_text, (20, 40))
    screen.blit(dist_text, (20, 70))
    screen.blit(label, (SCREEN_WIDTH // 2 - 80, 40))


def draw_sweep_line(angle):
    """Moving sweep line"""
    rad_angle = math.radians(angle - 180)
    end_x = RADAR_CENTER_X + RADAR_RADIUS * math.cos(rad_angle)
    end_y = RADAR_CENTER_Y + RADAR_RADIUS * math.sin(rad_angle)
    pygame.draw.line(screen, GREEN, (RADAR_CENTER_X, RADAR_CENTER_Y), (end_x, end_y), 2)


def draw_detected_points():
    """Red dots - detected objects"""
    global point_history
    max_dist = 20.0
    if 0 < current_distance < max_dist:
        rad_angle = math.radians(current_angle - 180)
        mapped_dist = (current_distance / max_dist) * RADAR_RADIUS
        point_x = RADAR_CENTER_X + mapped_dist * math.cos(rad_angle)
        point_y = RADAR_CENTER_Y + mapped_dist * math.sin(rad_angle)
        point_history.append({'x': point_x, 'y': point_y, 'age': 255})

    # Draw history (with fade effect)
    new_history = []
    for p in point_history:
        color = (0, p['age'], 0)
        pygame.draw.circle(screen, color, (int(p['x']), int(p['y'])), 3)
        p['age'] -= 2
        if p['age'] > 0:
            new_history.append(p)
    point_history = new_history


def read_serial():
    """Read data from Arduino"""
    global current_angle, current_distance
    if ser and ser.in_waiting:
        try:
            line = ser.readline().decode().strip()
            # Remove dot at the end and split by comma
            if line.endswith('.'):
                line = line[:-1]  # Remove last character (dot)
            
            if ',' in line:
                parts = line.split(',')
                if len(parts) == 2:
                    current_angle = int(parts[0])
                    current_distance = int(parts[1])
                    print(f"Angle: {current_angle}, Distance: {current_distance}")  # For debugging
        except (ValueError, UnicodeDecodeError) as e:
            print(f"Parse error: {e}, received string: '{line}'")
        except Exception as e:
            print(f"Other error: {e}")


# --- Main loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    read_serial()
    draw_radar_grid()
    draw_text()
    draw_sweep_line(current_angle)
    draw_detected_points()

    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()