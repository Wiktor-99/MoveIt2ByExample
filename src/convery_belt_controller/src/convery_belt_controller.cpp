#include <chrono>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float64.hpp"

class ConveryBeltController : public rclcpp::Node {
public:
  ConveryBeltController() : Node{"convery_belt_controller"} {
    using namespace std::chrono_literals;
    publisher_ =
        create_publisher<std_msgs::msg::Float64>("/conveyor/cmd_vel", 10);
    timer_ = create_wall_timer(1s, [this]() { timer_callback(); });
  }

private:
  void timer_callback() {
    auto message = std_msgs::msg::Float64();
    if (not started) {
      message.data = 0.5;
      started = true;
    } else {
      message.data = 0.0;
      started = false;
    }
    publisher_->publish(message);
  }

  bool started{};
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr publisher_;
};

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ConveryBeltController>());
  rclcpp::shutdown();
  return 0;
}
