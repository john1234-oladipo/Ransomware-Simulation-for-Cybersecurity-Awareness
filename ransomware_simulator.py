import os
import time
import random
from datetime import datetime, timedelta
import webbrowser
import json
import base64

class RansomwareSimulator:
    def __init__(self):
        self.simulation_dir = "ransomware_simulation"
        self.fake_files = []
        self.fake_encrypted_files = []
        self.ransom_note = "!!! YOUR FILES HAVE BEEN ENCRYPTED !!!.txt"
        self.payment_address = "1Simu1BitcoinAddressForEducation"
        self.amount = random.randint(500, 2000)
        self.countdown_hours = 72
        self.deadline = datetime.now() + timedelta(hours=self.countdown_hours)
        # Educational resources
        self.education_links = {
            "CISA Ransomware Guide": "https://www.cisa.gov/stopransomware",
            "No More Ransom Project": "https://www.nomoreransom.org/",
            "FTC Ransomware Info": "https://www.consumer.ftc.gov/articles/how-protect-yourself-ransomware"
        }

    def create_simulation_environment(self):
        """Create a safe simulation environment with fake files"""
        if not os.path.exists(self.simulation_dir):
            os.makedirs(self.simulation_dir)
            
        # Create some fake files to "encrypt"
        file_types = [
            ("document", ".docx"),
            ("spreadsheet", ".xlsx"),
            ("presentation", ".pptx"),
            ("photo", ".jpg"),
            ("video", ".mp4"),
            ("database", ".sql")
        ]
        
        for i in range(1, 11):  # Create 10 fake files
            file_type, ext = random.choice(file_types)
            filename = f"{file_type}_{i}{ext}"
            filepath = os.path.join(self.simulation_dir, filename)
            
            with open(filepath, "w") as f:
                f.write(f"This is a simulated {file_type} file. In a real attack, this would be encrypted.\n")
                f.write(f"File #{i} created for ransomware simulation purposes.\n")
            
            self.fake_files.append(filepath)
        
        print(f"\nCreated simulation environment with {len(self.fake_files)} fake files in '{self.simulation_dir}' directory.")

    def simulate_encryption(self):
        """Simulate the file encryption process (no actual encryption occurs)"""
        print("\n=== SIMULATING RANSOMWARE ATTACK ===")
        print("This is just a simulation - no files are actually being encrypted.")
        
        for filepath in self.fake_files:
            # Simulate "encryption" by creating new files with .encrypted extension
            encrypted_path = filepath + ".encrypted"
            
            # In a real attack, the file would be encrypted here
            # For simulation, we just copy the content with a warning
            with open(filepath, "r") as original, open(encrypted_path, "w") as encrypted:
                encrypted.write(f"SIMULATION: This file would be encrypted in a real attack.\n")
                encrypted.write(f"Original content from {os.path.basename(filepath)}:\n\n")
                encrypted.write(original.read())
            
            # "Delete" the original (just for simulation)
            os.remove(filepath)
            self.fake_encrypted_files.append(encrypted_path)
            
            print(f"Simulated encryption of {os.path.basename(filepath)}")
            time.sleep(0.2)  # Dramatic effect
        
        # Create ransom note
        self.create_ransom_note()
        
        print("\nSimulation complete! All files in the simulation directory appear encrypted.")
        print(f"Ransom note created: {os.path.join(self.simulation_dir, self.ransom_note)}")

    def create_ransom_note(self):
        """Create a fake ransom note with educational information"""
        note_path = os.path.join(self.simulation_dir, self.ransom_note)
        
        with open(note_path, "w") as note:
            note.write("""
            WARNING: This is a ransomware simulation for educational purposes
            
            In a real ransomware attack, your files would actually be encrypted right now.
            This is just a demonstration to show how ransomware works.
            
            ===== IF THIS WERE REAL =====
            All your files have been encrypted with military-grade AES-256 encryption!
            
            To recover your files, you must pay $%d in Bitcoin to: %s
            
            You have %d hours to pay. After that, the price will double.
            Deadline: %s
            
            ===== IMPORTANT: THIS IS A SIMULATION =====
            No files were actually encrypted. This is an educational tool to:
            - Show how ransomware attacks work
            - Demonstrate the importance of backups
            - Teach cybersecurity best practices
            
            === HOW TO PROTECT YOURSELF ===
            1. Regularly back up your files (3-2-1 rule: 3 copies, 2 media types, 1 offsite)
            2. Keep your software updated
            3. Be cautious with email attachments and links
            4. Use antivirus software
            5. Educate yourself about cybersecurity
            
            For more information, run the recovery simulation or visit:
            """ % (self.amount, self.payment_address, self.countdown_hours, self.deadline.strftime("%Y-%m-%d %H:%M:%S")))
            
            for name, url in self.education_links.items():
                note.write(f"\n- {name}: {url}")
        
    def simulate_recovery(self):
        """Simulate file recovery (either through payment or backups)"""
        print("\n=== RANSOMWARE RECOVERY OPTIONS ===")
        print("1. Simulate paying the ransom (not recommended in real life)")
        print("2. Simulate restoring from backups (recommended best practice)")
        print("3. Learn about ransomware protection")
        
        choice = input("\nSelect an option to simulate (1-3): ")
        
        if choice == "1":
            self.simulate_payment()
        elif choice == "2":
            self.simulate_backup_restore()
        elif choice == "3":
            self.show_educational_resources()
        else:
            print("Invalid choice. Please try again.")
            self.simulate_recovery()
    
    def simulate_payment(self):
        """Simulate paying the ransom (with educational warnings)"""
        print("\n=== SIMULATING RANSOM PAYMENT ===")
        print("WARNING: In real life, paying the ransom is NOT recommended because:")
        print("- There's no guarantee you'll get your files back")
        print("- It funds criminal organizations")
        print("- You may be targeted again")
        
        input("\nPress Enter to continue with simulation...")
        
        print(f"\nSending {self.amount} BTC to {self.payment_address}...")
        time.sleep(2)
        print("Waiting for payment confirmation...")
        time.sleep(3)
        
        # Simulate decryption
        for encrypted_path in self.fake_encrypted_files:
            original_path = encrypted_path.replace(".encrypted", "")
            
            with open(encrypted_path, "r") as encrypted, open(original_path, "w") as original:
                # Skip the first two simulation lines
                content = encrypted.readlines()[2:]
                original.writelines(content)
            
            os.remove(encrypted_path)
            print(f"Simulated decryption of {os.path.basename(original_path)}")
            time.sleep(0.1)
        
        print("\nFiles have been simulated to be restored (but remember, in real life this isn't guaranteed!).")
        print("The better solution is to restore from backups as shown in option 2.")
        
        self.show_educational_resources()
    
    def simulate_backup_restore(self):
        """Simulate restoring files from backups (the recommended approach)"""
        print("\n=== SIMULATING BACKUP RESTORATION ===")
        print("This is the recommended way to recover from ransomware!")
        print("The 3-2-1 backup rule recommends:")
        print("- 3 copies of your data")
        print("- 2 different media types")
        print("- 1 copy offsite")
        
        input("\nPress Enter to continue with simulation...")
        
        print("\nRestoring files from backup...")
        time.sleep(2)
        
        for encrypted_path in self.fake_encrypted_files:
            original_path = encrypted_path.replace(".encrypted", "")
            
            # Just create a new file to simulate restore from backup
            with open(original_path, "w") as f:
                f.write(f"This file was restored from backup simulation.\n")
                f.write(f"Original content would be restored from your actual backup.\n")
            
            os.remove(encrypted_path)
            print(f"Simulated restore of {os.path.basename(original_path)} from backup")
            time.sleep(0.1)
        
        print("\nFiles have been simulated to be restored from backup!")
        print("This demonstrates why regular backups are the best defense against ransomware.")
        
        self.show_educational_resources()
    
    def show_educational_resources(self):
        """Show educational resources about ransomware protection"""
        print("\n=== EDUCATIONAL RESOURCES ===")
        print("Learn more about ransomware protection at these resources:")
        
        for name, url in self.education_links.items():
            print(f"\n{name}: {url}")
        
        choice = input("\nWould you like to open any of these in your browser? (y/n): ").lower()
        if choice == "y":
            print("\nAvailable resources:")
            resources = list(self.education_links.items())
            for i, (name, url) in enumerate(resources, 1):
                print(f"{i}. {name}")
            
            try:
                selection = int(input("\nEnter number to open (1-%d): " % len(resources)))
                if 1 <= selection <= len(resources):
                    webbrowser.open(resources[selection-1][1])
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a number.")
    
    def cleanup(self):
        """Clean up the simulation environment"""
        if os.path.exists(self.simulation_dir):
            for file in os.listdir(self.simulation_dir):
                os.remove(os.path.join(self.simulation_dir, file))
            os.rmdir(self.simulation_dir)
            print("\nSimulation environment cleaned up.")

def main():
    print("""
    ==============================
    RANSOMWARE SIMULATOR (EDUCATIONAL)
    ==============================
    
    This is a harmless simulation designed to:
    - Demonstrate how ransomware attacks work
    - Show the importance of regular backups
    - Teach cybersecurity best practices
    
    NO FILES WILL BE ACTUALLY ENCRYPTED!
    All operations occur in a temporary simulation directory.
    """)
    
    simulator = RansomwareSimulator()
    
    try:
        simulator.create_simulation_environment()
        input("\nPress Enter to begin the ransomware simulation...")
        simulator.simulate_encryption()
        
        print("\n=== WHAT WOULD YOU DO? ===")
        print("This simulation shows what happens during a ransomware attack.")
        print("Let's explore recovery options (simulated).")
        
        simulator.simulate_recovery()
        
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
    finally:
        simulator.cleanup()
        print("\nEducational reminder: Always maintain regular backups of your important files!")
        print("Learn more about ransomware protection at:")
        for name, url in simulator.education_links.items():
            print(f"- {name}: {url}")

if __name__ == "__main__":
    main()
