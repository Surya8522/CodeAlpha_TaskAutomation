import os
import shutil

source_folder = "source"

destination_folder = "destination"

os.makedirs(destination_folder, exist_ok=True)

moved_count = 0

for file in os.listdir(source_folder):

    if file.lower().endswith(".jpg"):

        source_path = os.path.join(
            source_folder,
            file
        )

        destination_path = os.path.join(
            destination_folder,
            file
        )

        shutil.move(
            source_path,
            destination_path
        )

        moved_count += 1

print("================================")
print(" TASK AUTOMATION COMPLETED")
print("================================")
print(
    f"{moved_count} JPG files moved successfully."
)