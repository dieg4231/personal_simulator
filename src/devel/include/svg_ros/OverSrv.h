// Generated by gencpp from file svg_ros/OverSrv.msg
// DO NOT EDIT!


#ifndef SVG_ROS_MESSAGE_OVERSRV_H
#define SVG_ROS_MESSAGE_OVERSRV_H

#include <ros/service_traits.h>


#include <svg_ros/OverSrvRequest.h>
#include <svg_ros/OverSrvResponse.h>


namespace svg_ros
{

struct OverSrv
{

typedef OverSrvRequest Request;
typedef OverSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct OverSrv
} // namespace svg_ros


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::svg_ros::OverSrv > {
  static const char* value()
  {
    return "ed5c22717a93863499734f374ca8e9a3";
  }

  static const char* value(const ::svg_ros::OverSrv&) { return value(); }
};

template<>
struct DataType< ::svg_ros::OverSrv > {
  static const char* value()
  {
    return "svg_ros/OverSrv";
  }

  static const char* value(const ::svg_ros::OverSrv&) { return value(); }
};


// service_traits::MD5Sum< ::svg_ros::OverSrvRequest> should match 
// service_traits::MD5Sum< ::svg_ros::OverSrv > 
template<>
struct MD5Sum< ::svg_ros::OverSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::svg_ros::OverSrv >::value();
  }
  static const char* value(const ::svg_ros::OverSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::svg_ros::OverSrvRequest> should match 
// service_traits::DataType< ::svg_ros::OverSrv > 
template<>
struct DataType< ::svg_ros::OverSrvRequest>
{
  static const char* value()
  {
    return DataType< ::svg_ros::OverSrv >::value();
  }
  static const char* value(const ::svg_ros::OverSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::svg_ros::OverSrvResponse> should match 
// service_traits::MD5Sum< ::svg_ros::OverSrv > 
template<>
struct MD5Sum< ::svg_ros::OverSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::svg_ros::OverSrv >::value();
  }
  static const char* value(const ::svg_ros::OverSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::svg_ros::OverSrvResponse> should match 
// service_traits::DataType< ::svg_ros::OverSrv > 
template<>
struct DataType< ::svg_ros::OverSrvResponse>
{
  static const char* value()
  {
    return DataType< ::svg_ros::OverSrv >::value();
  }
  static const char* value(const ::svg_ros::OverSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // SVG_ROS_MESSAGE_OVERSRV_H