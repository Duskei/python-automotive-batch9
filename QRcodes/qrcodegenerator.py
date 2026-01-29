import qrcode # python library for generating QR codes
import csv # built-in library for handling CSV files
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
def generate_dynamic_qr():
    # Ask the user for the number of students
    while True: 
        #try-except block to ensure valid integer input
        try:
            num_students = int(input("How many students do you want to enter? "))
            if num_students > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    all_members_data = [] # define list to hold all student data
    csv_filename = "student_records.csv"

    # 1. Collect data based on user input
    for i in range(1, num_students + 1):
        print(f"\n--- Details for Student {i} of {num_students} ---")
        id_num = input("ID Number: ")
        name = input("Name: ")
        subject = input("Subject: ")
        score = input("Score: ")
        
        all_members_data.append({
            "ID": id_num,
            "Name": name,
            "Subject": subject,
            "Score": score
        })
#-------------------------------------------1-----------------------------------------------------------
    # 2. Save all data to a CSV file
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Subject", "Score"])
        writer.writeheader()
        writer.writerows(all_members_data)

    # 3. Format the data for the QR code
    # Using a structured format makes it readable upon scanning
    qr_string = f"Total Students: {num_students}\n" + "="*20 + "\n" # Header
    # Append each student's data to the QR string
    for member in all_members_data:
        qr_string += f"ID: {member['ID']} | {member['Name']} | {member['Subject']}: {member['Score']}\n"
#-------------------------------------------2-----------------------------------------------------------
    # 4. Generate the QR code
    qr = qrcode.QRCode(
        version=None, # automatic size
        error_correction=qrcode.constants.ERROR_CORRECT_M, 
        # This means the QR code can still be scanned even if its surface is dirty or damaged
        box_size=10, #defines how many pixels each small square (module) in the QR code will be
        border=4, #sets the thickness of the white margin around the QR code
    )
    qr.add_data(qr_string) #loads the formatted string into the QR code object
    qr.make(fit=True) #computes the optimal size for the QR code based on the data

    img = img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(), # Makes dots rounded
    color_mask=RadialGradiantColorMask(back_color=(255, 255, 255), center_color=(0, 102, 204), edge_color=(0, 0, 0)) # Adds a blue-to-black gradient
)
    img.save("group_results_qr.png")

    print(f"\n--- Done! ---")
    print(f"1. Spreadsheet created: {csv_filename}")
    print(f"2. QR Code created: group_results_qr.png")

if __name__ == "__main__":
    generate_dynamic_qr()