import os
import wx

tos_text = """
Terms of Service (TOS)

1. Introduction
Welcome to the Eggman Empire! By accessing or using our platform, you agree to these Terms of Service. If you do not agree, please refrain from using our services.

2. Eligibility
You must be at least 13 years old to use our services. If you are under the age of majority in your jurisdiction, parental consent is required.

3. User Conduct
Users agree not to:
- Use the platform for illegal activities.
- Attempt to hack, disrupt, or damage the service.
- Share misleading or harmful content.

Violations may result in suspension or termination of access.

4. Intellectual Property
All content, trademarks, and logos on the Eggman Empire platform are the property of the Empire unless otherwise stated. You may not copy, distribute, or reproduce this content without permission.

5. Disclaimer of Warranties
The platform is provided \"as is.\" We make no guarantees regarding uptime, functionality, or fitness for a particular purpose.

6. Limitation of Liability
The Eggman Empire is not liable for any damages or losses resulting from your use of the platform.

7. Changes to the TOS
We may update these Terms of Service occasionally. Continued use of the platform constitutes acceptance of any changes.

8. Contact Us
For questions or concerns, please contact us at support@eggmanempire.com.
"""

privacy_policy_text = """
Privacy Policy

1. Introduction
The Eggman Empire values your privacy. This Privacy Policy explains how we handle your personal information.

2. Data Collection
We only collect the data necessary to provide our services, including:
- Account details (e.g., username, email).
- Usage data (e.g., log-ins, preferences).

3. Data Use
Collected data is used exclusively for:
- Improving the platform.
- Personalizing user experiences.
- Providing technical support.

We will **never** sell, rent, or share your data with third parties for profit.

4. Cookies and Analytics
We use cookies to enhance functionality and understand user behavior. You may disable cookies in your browser settings, but some features may not function as intended.

5. Data Security
We employ robust measures to protect your data, including encryption and access control. However, no system is 100% secure, and we cannot guarantee absolute security.

6. User Rights
You have the right to:
- Access your data.
- Request corrections or deletions.
- Opt-out of non-essential communications.

To exercise these rights, email us at privacy@eggmanempire.com.

7. Third-Party Links
Our platform may contain links to third-party sites. We are not responsible for their content or privacy practices.

8. Changes to the Privacy Policy
We may update this policy periodically. Continued use of the platform signifies acceptance of any updates.

9. Contact Us
For privacy inquiries, contact us at privacy@eggmanempire.com.
"""

print("Eggman Empire Terms of Service:\n")
print(tos_text)
print("\nEggman Empire Privacy Policy:\n")
print(privacy_policy_text)

import tkinter as tk
from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk  # Import Pillow for image handling

def show_custom_warning():
    # Create a custom warning window
    warning_window = Toplevel(root)
    warning_window.title("TOS 0.01")
    warning_window.geometry("350x200")
    warning_window.configure(bg="White")

    # Load and display the image using Pillow
    img = Image.open("E:/Eggman empire/eggnet/App/MetalSonic3.png")
    img = img.resize((100, 100))  # Resize for better display
    img_tk = ImageTk.PhotoImage(img)

    image_label = Label(warning_window, image=img_tk, bg="White")
    image_label.image = img_tk  # Keep a reference to avoid garbage collection
    image_label.pack(pady=5)

    # Display a warning message
    message_label = Label(
        warning_window, text="are you wanting to agree?", font=("Arial", 14), bg="white"
    )
    message_label.pack()

    # Close the entire application 2 seconds after clicking OK
    def stop_program():
        root.after(2000, root.destroy)  # Close entire program after 2 seconds

    Button(warning_window, text="yes", command=stop_program2).pack(pady=10)
    Button(warning_window, text="no", command=stop_program).pack(pady=10)

    def stop_program2(self):
     import Net_Test_6

root = tk.Tk()
root.title("Main Window")

Button(root, text="Show Warning", command=show_custom_warning).pack(pady=20)

root.mainloop()

