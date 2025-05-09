from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(filename, width, height, text):
    # Create a new image with a gradient background
    image = Image.new('RGB', (width, height), '#f8f9fa')
    draw = ImageDraw.Draw(image)
    
    # Draw a simple pattern
    for i in range(0, width, 20):
        draw.line([(i, 0), (i, height)], fill='#e9ecef', width=1)
    for i in range(0, height, 20):
        draw.line([(0, i), (width, i)], fill='#e9ecef', width=1)
    
    # Add text
    try:
        font = ImageFont.truetype('arial.ttf', 40)
    except:
        font = ImageFont.load_default()
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, fill='#6c757d', font=font)
    
    # Save the image
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    image.save(filename, 'JPEG', quality=85)

def main():
    # Create directories
    base_dir = 'static/images'
    os.makedirs(f'{base_dir}/profile', exist_ok=True)
    os.makedirs(f'{base_dir}/projects', exist_ok=True)
    
    # Create profile placeholder
    create_placeholder_image(
        f'{base_dir}/profile/profile-placeholder.jpg',
        800, 800,
        'Profile'
    )
    
    # Create project placeholders
    project_titles = [
        'Soft Robotics',
        'Human-Robot Interaction',
        'Swarm Robotics',
        'Computer Vision',
        'Product Management',
        'Research'
    ]
    
    for i, title in enumerate(project_titles, 1):
        create_placeholder_image(
            f'{base_dir}/projects/project{i}.jpg',
            800, 600,
            title
        )

if __name__ == '__main__':
    main() 