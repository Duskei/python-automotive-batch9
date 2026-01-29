import qrcode

qr_content = """GROUP: Group 2

========================
Name: Muskan
GitHub:
https://github.com/Muskan271503/
LinkedIn:
https://www.linkedin.com/in/muskan-r-2a3613221/

========================
Name: Vivek
GitHub:
https://github.com/Vivek9988
LinkedIn:
https://www.linkedin.com/in/vivek022/

========================
Name: Gnana Prasanna
GitHub:
https://github.com/GnanaPrasanna1925
LinkedIn:
https://www.linkedin.com/in/k-gnana-prasanna-71ab91285/

========================
Name: Sri Harshith
GitHub:
https://github.com/sriharshith1403
LinkedIn:
https://www.linkedin.com/in/adatravu-sri-harshith-659051234/

========================
Name: Srestha
GitHub:
https://github.com/Duskei
LinkedIn:
https://www.linkedin.com/in/srestha-nath-b6a2ba304/

========================
Name: Srija
GitHub:
https://github.com/srijachalumuri
LinkedIn:
https://www.linkedin.com/in/srija-chalumuri-230189296/
"""

qr = qrcode.QRCode(
    version=3,  # slightly larger to fit all data
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(qr_content)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("Group2_AllMembers_Profile_QR.png")

print("✅ ONE QR generated for all group members")
print("Scan with ANY phone to view all names + GitHub + LinkedIn")