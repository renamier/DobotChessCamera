
from serial.tools import list_ports
import pydobot

class RobotArmControl:
      #constructor
    def __init__(self,port):
        self.port = port
        self.device = None 
        #port = 'COM3'
        self.is_connected = False
        #self.connect_dobot()

    #def connect_dobot(self):
        
        #try:
           # self.device =pydobot.Dobot(port=self.port)
           # print(f"Dobot connected on port {self.port}")
        #except Exception as e:
            #print(f"An error occurred: {e}")
 

#available_ports = list_ports.comports()
#print(f'available ports: {[x.device for x in available_ports]}')
#port = 'COM3'

#device = pydobot.Dobot(port=port, verbose=False)
        
    def connect_dobot(self):
        if not self.is_connected:
            try:
                self.device = pydobot.Dobot(port=self.port, verbose=True)
                self.is_connected = True
                print("Connected to the device successfully.")
           
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Device is already connected.") 
        
         
  

    def chess_position_to_coordinates(self, position):  
      coordinates = {'a1':{'x1': +309.81, 'y1': -077.00, 'z1': +025.00, 'r1': -55.00},
                    'a2':{'x1': +287.98, 'y1': -077.28, 'z1': +025.00, 'r1': -55.00},
                    'a3':{'x1': +266.15, 'y1': -077.57, 'z1': +025.00, 'r1': -55.00},
                    'a4':{'x1': +244.32, 'y1': -077.86, 'z1': +025.00, 'r1': -55.00},
                    'a5':{'x1': +222.49, 'y1': -078.14, 'z1': +025.00, 'r1': -55.00},
                    'a6':{'x1': +200.66, 'y1': -078.43, 'z1': +025.00, 'r1': -55.00},
                    'a7':{'x1': +178.83, 'y1': -078.72, 'z1': +025.00, 'r1': -55.00},
                    'a8':{'x1': +157.00, 'y1': -079.00, 'z1': +025.00, 'r1': -55.00},
                    'b1':{'x1': +309.81, 'y1': -054.71, 'z1': +025.00, 'r1': -55.00},
                    'b2':{'x1': +287.98, 'y1': -054.96, 'z1': +025.00, 'r1': -55.00},
                    'b3':{'x1': +266.15, 'y1': -055.20, 'z1': +025.00, 'r1': -55.00},
                    'b4':{'x1': +244.32, 'y1': -055.45, 'z1': +025.00, 'r1': -55.00},
                    'b5':{'x1': +222.49, 'y1': -055.69, 'z1': +025.00, 'r1': -55.00},
                    'b6':{'x1': +200.66, 'y1': -055.94, 'z1': +025.00, 'r1': -55.00},
                    'b7':{'x1': +178.83, 'y1': -056.19, 'z1': +025.00, 'r1': -55.00},
                    'b8':{'x1': +157.00, 'y1': -056.43, 'z1': +025.00, 'r1': -55.00},
                    'c1':{'x1': +309.81, 'y1': -032.43, 'z1': +025.00, 'r1': -55.00},
                    'c2':{'x1': +287.98, 'y1': -032.63, 'z1': +025.00, 'r1': -55.00},
                    'c3':{'x1': +266.15, 'y1': -032.84, 'z1': +025.00, 'r1': -55.00},
                    'c4':{'x1': +244.32, 'y1': -033.04, 'z1': +025.00, 'r1': -55.00},
                    'c5':{'x1': +222.49, 'y1': -033.25, 'z1': +025.00, 'r1': -55.00},
                    'c6':{'x1': +200.66, 'y1': -033.45, 'z1': +025.00, 'r1': -55.00},
                    'c7':{'x1': +178.83, 'y1': -033.66, 'z1': +025.00, 'r1': -55.00},
                    'c8':{'x1': +157.00, 'y1': -033.86, 'z1': +025.00, 'r1': -55.00},
                    'd1':{'x1': +309.81, 'y1': -010.14, 'z1': +025.00, 'r1': -55.00},
                    'd2':{'x1': +287.98, 'y1': -010.30, 'z1': +025.00, 'r1': -55.00},
                    'd3':{'x1': +266.15, 'y1': -010.47, 'z1': +025.00, 'r1': -55.00},
                    'd4':{'x1': +244.32, 'y1': -010.63, 'z1': +025.00, 'r1': -55.00},
                    'd5':{'x1': +222.49, 'y1': -010.80, 'z1': +025.00, 'r1': -55.00},
                    'd6':{'x1': +200.66, 'y1': -010.96, 'z1': +025.00, 'r1': -55.00},
                    'd7':{'x1': +178.83, 'y1': -011.12, 'z1': +025.00, 'r1': -55.00},
                    'd8':{'x1': +157.00, 'y1': -011.29, 'z1': +025.00, 'r1': -55.00},
                    'e1':{'x1': +309.81, 'y1': +012.15, 'z1': +025.00, 'r1': -55.00},
                    'e2':{'x1': +287.98, 'y1': +012.02, 'z1': +025.00, 'r1': -55.00},
                    'e3':{'x1': +266.15, 'y1': +011.90, 'z1': +025.00, 'r1': -55.00},
                    'e4':{'x1': +244.32, 'y1': +011.78, 'z1': +025.00, 'r1': -55.00},
                    'e5':{'x1': +222.49, 'y1': +011.65, 'z1': +025.00, 'r1': -55.00},
                    'e6':{'x1': +200.66, 'y1': +011.53, 'z1': +025.00, 'r1': -55.00},
                    'e7':{'x1': +178.83, 'y1': +011.41, 'z1': +025.00, 'r1': -55.00},
                    'e8':{'x1': +157.00, 'y1': +011.28, 'z1': +025.00, 'r1': -55.00},
                    'f1':{'x1': +309.81, 'y1': +034.43, 'z1': +025.00, 'r1': -55.00},
                    'f2':{'x1': +287.98, 'y1': +034.35, 'z1': +025.00, 'r1': -55.00},
                    'f3':{'x1': +266.15, 'y1': +034.27, 'z1': +025.00, 'r1': -55.00},
                    'f4':{'x1': +244.32, 'y1': +034.18, 'z1': +025.00, 'r1': -55.00},
                    'f5':{'x1': +222.49, 'y1': +034.10, 'z1': +025.00, 'r1': -55.00},
                    'f6':{'x1': +200.66, 'y1': +034.02, 'z1': +025.00, 'r1': -55.00},
                    'f7':{'x1': +178.83, 'y1': +033.94, 'z1': +025.00, 'r1': -55.00},
                    'f8':{'x1': +157.00, 'y1': +033.86, 'z1': +025.00, 'r1': -55.00},
                    'g1':{'x1': +309.81, 'y1': +056.72, 'z1': +025.00, 'r1': -55.00},
                    'g2':{'x1': +287.98, 'y1': +056.67, 'z1': +025.00, 'r1': -55.00},
                    'g3':{'x1': +266.15, 'y1': +056.63, 'z1': +025.00, 'r1': -55.00},
                    'g4':{'x1': +244.32, 'y1': +056.59, 'z1': +025.00, 'r1': -55.00},
                    'g5':{'x1': +222.49, 'y1': +056.55, 'z1': +025.00, 'r1': -55.00},
                    'g6':{'x1': +200.66, 'y1': +056.51, 'z1': +025.00, 'r1': -55.00},
                    'g7':{'x1': +178.83, 'y1': +056.47, 'z1': +025.00, 'r1': -55.00},
                    'g8':{'x1': +157.00, 'y1': +056.43, 'z1': +025.00, 'r1': -55.00},
                    'h1':{'x1': +309.81, 'y1': +079.00, 'z1': +025.00, 'r1': -55.00},
                    'h2':{'x1': +287.98, 'y1': +079.00, 'z1': +025.00, 'r1': -55.00},
                    'h3':{'x1': +266.15, 'y1': +079.00, 'z1': +025.00, 'r1': -55.00},
                    'h4':{'x1': +244.32, 'y1': +079.00, 'z1': +025.00, 'r1': -55.00},
                    'h5':{'x1': +222.49, 'y1': +079.00, 'z1': +025.00, 'r1': -55.00},
                    'h6':{'x1': +200.66, 'y1': +079.00, 'z1': +025.00, 'r1': -55.00},
                    'h7':{'x1': +178.83, 'y1': +079.00, 'z1': +025.00, 'r1': -55.00},
                    'h8':{'x1': +157.00, 'y1': +079.00, 'z1': +025.00, 'r1': -55.00}
                }
      return coordinates[position]

   
        
    def execute_move(self, position):
         self.connect_dobot()
         if self.is_connected:
             try:
                start_arm_coords = self.chess_position_to_coordinates(position[:2])
                end_arm_coords = self.chess_position_to_coordinates(position[2:4])

                print(start_arm_coords['x1'], start_arm_coords['y1'],start_arm_coords['z1'],start_arm_coords['r1'])
                self.device.move_to(float(start_arm_coords['x1']), float(start_arm_coords['y1']), float(start_arm_coords['z1']), float(start_arm_coords['r1']))
            
                # open gripper
                self.device.suck(True) # open the gripper
                self.device.grip(False)
                self.device.wait(500)
                self.device.suck(False)


                # drop down
                self.device.move_to(float(start_arm_coords['x1']), float(start_arm_coords['y1']), -30, float(start_arm_coords['r1']))

                # close gripper
                self.device.grip(True) # close the gripper
                self.device.wait(500)
                self.device.suck(False)

                # pull up
                self.device.move_to(float(start_arm_coords['x1']), float(start_arm_coords['y1']), 25, float(start_arm_coords['r1']))

            
                print(end_arm_coords['x1'], end_arm_coords['y1'],end_arm_coords['z1'],end_arm_coords['r1'] )
                self.device.move_to(float(end_arm_coords['x1']), float(end_arm_coords['y1']), float(end_arm_coords['z1']), float(end_arm_coords['r1']))


                # drop down
                self.device.move_to(float(end_arm_coords['x1']), float(end_arm_coords['y1']), -25, float(end_arm_coords['r1']))


                # open gripper
                self.device.suck(True) # open the gripper
                self.device.grip(False)
                self.device.wait(500)
                self.device.suck(False)

                # pull up
                self.device.move_to(float(end_arm_coords['x1']), float(end_arm_coords['y1']), 25, float(end_arm_coords['r1']))
                self.device.wait(500)
                self.device.move_to(+190.00, -190.00, +019.00, +043.00)

                # close gripper


                return True
             except Exception as e:
                print(f"An error occurred during move execution: {e}")
                return False

    
   
