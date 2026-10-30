import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class DuvarKacanNode(Node):
    def __init__(self):
        super().__init__('duvar_kacan_node')
        
        # Parametreler
        self.declare_parameter('linear_speed', 1.5)
        self.declare_parameter('angular_speed', 1.2)
        self.declare_parameter('min_limit', 1.0)
        self.declare_parameter('max_limit', 10.0)

        # Publisher & Subscriber
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription_ = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        self.timer_log = self.create_timer(1.0, self.log_callback)
        self.current_pose = None

    def pose_callback(self, msg):
        self.current_pose = msg
        
        linear_spd = self.get_parameter('linear_speed').value
        angular_spd = self.get_parameter('angular_speed').value
        min_lim = self.get_parameter('min_limit').value
        max_lim = self.get_parameter('max_limit').value

        cmd = Twist()

        # Duvar sınır kontrolü (Sınıra çarptığında hem hafif ileri gitsin hem dönsün)
        if msg.x < min_lim or msg.x > max_lim or msg.y < min_lim or msg.y > max_lim:
            cmd.linear.x = 0.5  # Sıkışmaması için hafif ileri hız veriyoruz
            cmd.angular.z = angular_spd
        else:
            cmd.linear.x = linear_spd
            cmd.angular.z = 0.0

        self.publisher_.publish(cmd)

    def log_callback(self):
        if self.current_pose is not None:
            self.get_logger().info(
                f"Konum -> X: {self.current_pose.x:.2f}, Y: {self.current_pose.y:.2f}"
            )

def main(args=None):
    rclpy.init(args=args)
    node = DuvarKacanNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
