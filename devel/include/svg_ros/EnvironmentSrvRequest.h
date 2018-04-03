// Generated by gencpp from file svg_ros/EnvironmentSrvRequest.msg
// DO NOT EDIT!


#ifndef SVG_ROS_MESSAGE_ENVIRONMENTSRVREQUEST_H
#define SVG_ROS_MESSAGE_ENVIRONMENTSRVREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace svg_ros
{
template <class ContainerAllocator>
struct EnvironmentSrvRequest_
{
  typedef EnvironmentSrvRequest_<ContainerAllocator> Type;

  EnvironmentSrvRequest_()
    : param()  {
    }
  EnvironmentSrvRequest_(const ContainerAllocator& _alloc)
    : param(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _param_type;
  _param_type param;




  typedef boost::shared_ptr< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> const> ConstPtr;

}; // struct EnvironmentSrvRequest_

typedef ::svg_ros::EnvironmentSrvRequest_<std::allocator<void> > EnvironmentSrvRequest;

typedef boost::shared_ptr< ::svg_ros::EnvironmentSrvRequest > EnvironmentSrvRequestPtr;
typedef boost::shared_ptr< ::svg_ros::EnvironmentSrvRequest const> EnvironmentSrvRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace svg_ros

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eb04b7504512676dca105ab8842899a4";
  }

  static const char* value(const ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeb04b7504512676dULL;
  static const uint64_t static_value2 = 0xca105ab8842899a4ULL;
};

template<class ContainerAllocator>
struct DataType< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "svg_ros/EnvironmentSrvRequest";
  }

  static const char* value(const ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string param\n\
";
  }

  static const char* value(const ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.param);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct EnvironmentSrvRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::svg_ros::EnvironmentSrvRequest_<ContainerAllocator>& v)
  {
    s << indent << "param: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.param);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SVG_ROS_MESSAGE_ENVIRONMENTSRVREQUEST_H
