import subprocess, os

BUILD = os.path.dirname(os.path.abspath(__file__))

for etapa in ["process_images.py", "gen_index.py", "gen_bio.py", "gen_og_image.py"]:
    print(f"\n--- {etapa} ---")
    subprocess.run(["python3", os.path.join(BUILD, etapa)], check=True)

print("\nOK — index.html + bio.html + og-image gerados.")
