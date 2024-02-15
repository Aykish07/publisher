import rclpy
from rclpy.node import Node
import random


from std_msgs.msg import ByteMultiArray




class MinimalPublisher(Node):


   def __init__(self):
       super().__init__('minimal_publisher')
       self.publisher_ = self.create_publisher(ByteMultiArray, 'data_hub', 10)
       timer_period = 0.5  # seconds
       self.timer = self.create_timer(timer_period, self.timer_callback)


   def timer_callback(self):
      
       msg_id_no = random.choice([10,19,24,79,83,201,212])
       msg_data_no = random.randint(1,110)
       msg_id_sim = msg_id_no.to_bytes(1, byteorder='big')
       msg_data_sim = msg_data_no.to_bytes(1,byteorder='big')


       msg = ByteMultiArray()
       msg.data = [msg_id_sim,msg_data_sim]
       self.publisher_.publish(msg)
       #self.get_logger().info('Publishing: "%s"' % str(msg.data))
       print(msg.data)
       print("ID = ",int.from_bytes(msg.data[0],'big'))
       print("Data = ",int.from_bytes(msg.data[1],'big'))


def main(args=None):
   rclpy.init(args=args)


   minimal_publisher = MinimalPublisher()


   rclpy.spin(minimal_publisher)


   # Destroy the node explicitly
   # (optional - otherwise it will be done automatically
   # when the garbage collector destroys the node object)
   minimal_publisher.destroy_node()
   rclpy.shutdown()




if __name__ == '__main__':
   main()

