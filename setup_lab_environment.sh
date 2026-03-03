#!/bin/bash
# setup_lab_environment.sh: Script to automate the creation and configuration of 3 virtual machines with VirtualBox

VBoxManage () {
  command VBoxManage "$@"
}

# Create three VMs
for i in {1..3}; do
  VM_NAME="AttackBehaviorSimulatorVM$i"
  # Create a new VM
  VBoxManage createvm --name "$VM_NAME" --register
  # Set memory and CPU
  VBoxManage modifyvm "$VM_NAME" --memory 2048 --cpus 2
  # Configure network
  VBoxManage modifyvm "$VM_NAME" --nic1 nat
  # Create and attach the virtual hard disk
  VBoxManage createhd --filename "${VM_NAME}.vdi" --size 20000
  VBoxManage storagectl "$VM_NAME" --name "SATA Controller" --add sata --controller IntelAHCI
  VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "${VM_NAME}.vdi"
  # Set the OS type
  VBoxManage modifyvm "$VM_NAME" --ostype Ubuntu_64
done

echo "3 VMs created and configured successfully!"