import autosar
import time
from datetime import datetime

class InfotainmentSimulator:
    def __init__(self):
        # Create a workspace
        self.ws = autosar.workspace(version="4.2.2")
        # Task 1: Create packages for organization
        self.if_package = self.ws.createPackage('Interfaces')
        self.swc_package = self.ws.createPackage('Infotainment')
        self.com_log = []
#-------------------------------------1----------------------------------------
    def create_mock_swcs(self):
        # Create SWCs and Interfaces with correct references
        
        # 1. Create the Interface for SWCs to communicate and define Data Elements
        audio_interface = self.if_package.createSenderReceiverInterface('AudioInterface')
        audio_interface.append(autosar.element.DataElement('VolumeLevel', 'uint8')) #add Data Element
        
        # 2. Define the Full Path to the Interface (Required by the library)
        interface_ref = '/Interfaces/AudioInterface'
        
        # 3. Create SWC 1: HMI (Sender)
        self.hmi_swc = self.swc_package.createApplicationSoftwareComponent('HMI_Component')
        # Using the full path reference here to fix the InvalidPortInterfaceRef error
        self.hmi_swc.createProvidePort('VolumeOut', interface_ref)
        
        # 4. Create SWC 2: Audio Controller (Receiver)
        self.audio_swc = self.swc_package.createApplicationSoftwareComponent('Audio_Controller')
        self.audio_swc.createRequirePort('VolumeIn', interface_ref)
        
        print("SUCCESS: SWCs linked to Interface via full workspace paths.")
#-------------------------------------2----------------------------------------
    def exchange_signals(self, volume_value):
        #Exchange signals and Log Timing
        # Start timing (Simulating the RTE start)
        start_time = time.perf_counter()
        
        # Simulate Middleware processing delay (5ms)
        time.sleep(0.005) 
        
        end_time = time.perf_counter()
        latency = (end_time - start_time) * 1000 
        
        # Log communication timing
        log_entry = {
            "timestamp": datetime.now().strftime('%H:%M:%S.%f'),
            "sender": "HMI_Component",
            "receiver": "Audio_Controller",
            "val": volume_value,
            "latency": f"{latency:.2f}ms"
        }
        self.com_log.append(log_entry)
        print(f"RTE: Signal 'VolumeLevel' delivered. Latency: {latency:.2f}ms")
#-------------------------------------3----------------------------------------
    def generate_timing_report(self):
        """Generate final report for submission."""
        print("\n" + "="*65)
        print("   AUTOSAR INFOTAINMENT MIDDLEWARE SIMULATOR REPORT")
        print("="*65)
        print(f"{'Timestamp':<18} | {'From -> To':<30} | {'Lat'}")
        print("-" * 65)
        for log in self.com_log:
            route = f"{log['sender']} -> {log['receiver']}"
            print(f"{log['timestamp']:<18} | {route:<30} | {log['latency']}")
        print("="*65)

# --- Execution ---
if __name__ == "__main__":
    sim = InfotainmentSimulator()
    sim.create_mock_swcs()

    # Simulate three user interactions
    sim.exchange_signals(10)
    sim.exchange_signals(25)
    sim.exchange_signals(50)

    sim.generate_timing_report()