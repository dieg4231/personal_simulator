// Generated by gencpp from file svg_ros/LightRealSrv.msg
// DO NOT EDIT!


#ifndef SVG_ROS_MESSAGE_LIGHTREALSRV_H
#define SVG_ROS_MESSAGE_LIGHTREALSRV_H

#include <ros/service_traits.h>


#include <svg_ros/LightRealSrvRequest.h>
#include <svg_ros/LightRealSrvResponse.h>


namespace svg_ros
{

struct LightRealSrv
{

typedef LightRealSrvRequest Request;
typedef LightRealSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct LightRealSrv
} // namespace svg_ros


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::svg_ros::LightRealSrv > {
  static const char* value()
  {
    return "880a7d45ae2b2447f4ed19a09614d287";
  }

  static const char* value(const ::svg_ros::LightRealSrv&) { return value(); }
};

template<>
struct DataType< ::svg_ros::LightRealSrv > {
  static const char* value()
  {
    return "svg_ros/LightRealSrv";
  }

  static const char* value(const ::svg_ros::LightRealSrv&) { return value(); }
};


// service_traits::MD5Sum< ::svg_ros::LightRealSrvRequest> should match 
// service_traits::MD5Sum< ::svg_ros::LightRealSrv > 
template<>
struct MD5Sum< ::svg_ros::LightRealSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::svg_ros::LightRealSrv >::value();
  }
  static const char* value(const ::svg_ros::LightRealSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::svg_ros::LightRealSrvRequest> should match 
// service_traits::DataType< ::svg_ros::LightRealSrv > 
template<>
struct DataType< ::svg_ros::LightRealSrvRequest>
{
  static const char* value()
  {
    return DataType< ::svg_ros::LightRealSrv >::value();
  }
  static const char* value(const ::svg_ros::LightRealSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::svg_ros::LightRealSrvResponse> should match 
// service_traits::MD5Sum< ::svg_ros::LightRealSrv > 
template<>
struct MD5Sum< ::svg_ros::LightRealSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::svg_ros::LightRealSrv >::value();
  }
  static const char* value(const ::svg_ros::LightRealSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::svg_ros::LightRealSrvResponse> should match 
// service_traits::DataType< ::svg_ros::LightRealSrv > 
template<>
struct DataType< ::svg_ros::LightRealSrvResponse>
{
  static const char* value()
  {
    return DataType< ::svg_ros::LightRealSrv >::value();
  }
  static const char* value(const ::svg_ros::LightRealSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // SVG_ROS_MESSAGE_LIGHTREALSRV_H