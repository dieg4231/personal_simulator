; Auto-generated. Do not edit!


(cl:in-package svg_ros-srv)


;//! \htmlinclude EnvironmentSrv-request.msg.html

(cl:defclass <EnvironmentSrv-request> (roslisp-msg-protocol:ros-message)
  ((param
    :reader param
    :initarg :param
    :type cl:string
    :initform ""))
)

(cl:defclass EnvironmentSrv-request (<EnvironmentSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EnvironmentSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EnvironmentSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name svg_ros-srv:<EnvironmentSrv-request> is deprecated: use svg_ros-srv:EnvironmentSrv-request instead.")))

(cl:ensure-generic-function 'param-val :lambda-list '(m))
(cl:defmethod param-val ((m <EnvironmentSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader svg_ros-srv:param-val is deprecated.  Use svg_ros-srv:param instead.")
  (param m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EnvironmentSrv-request>) ostream)
  "Serializes a message object of type '<EnvironmentSrv-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'param))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'param))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EnvironmentSrv-request>) istream)
  "Deserializes a message object of type '<EnvironmentSrv-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'param) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'param) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EnvironmentSrv-request>)))
  "Returns string type for a service object of type '<EnvironmentSrv-request>"
  "svg_ros/EnvironmentSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EnvironmentSrv-request)))
  "Returns string type for a service object of type 'EnvironmentSrv-request"
  "svg_ros/EnvironmentSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EnvironmentSrv-request>)))
  "Returns md5sum for a message object of type '<EnvironmentSrv-request>"
  "caeffbf51b8bc21c7838947aa06fdc32")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EnvironmentSrv-request)))
  "Returns md5sum for a message object of type 'EnvironmentSrv-request"
  "caeffbf51b8bc21c7838947aa06fdc32")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EnvironmentSrv-request>)))
  "Returns full string definition for message of type '<EnvironmentSrv-request>"
  (cl:format cl:nil "string param~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EnvironmentSrv-request)))
  "Returns full string definition for message of type 'EnvironmentSrv-request"
  (cl:format cl:nil "string param~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EnvironmentSrv-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'param))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EnvironmentSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'EnvironmentSrv-request
    (cl:cons ':param (param msg))
))
;//! \htmlinclude EnvironmentSrv-response.msg.html

(cl:defclass <EnvironmentSrv-response> (roslisp-msg-protocol:ros-message)
  ((sensor
    :reader sensor
    :initarg :sensor
    :type cl:integer
    :initform 0)
   (light
    :reader light
    :initarg :light
    :type cl:integer
    :initform 0)
   (base
    :reader base
    :initarg :base
    :type cl:integer
    :initform 0)
   (invert
    :reader invert
    :initarg :invert
    :type cl:integer
    :initform 0))
)

(cl:defclass EnvironmentSrv-response (<EnvironmentSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EnvironmentSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EnvironmentSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name svg_ros-srv:<EnvironmentSrv-response> is deprecated: use svg_ros-srv:EnvironmentSrv-response instead.")))

(cl:ensure-generic-function 'sensor-val :lambda-list '(m))
(cl:defmethod sensor-val ((m <EnvironmentSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader svg_ros-srv:sensor-val is deprecated.  Use svg_ros-srv:sensor instead.")
  (sensor m))

(cl:ensure-generic-function 'light-val :lambda-list '(m))
(cl:defmethod light-val ((m <EnvironmentSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader svg_ros-srv:light-val is deprecated.  Use svg_ros-srv:light instead.")
  (light m))

(cl:ensure-generic-function 'base-val :lambda-list '(m))
(cl:defmethod base-val ((m <EnvironmentSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader svg_ros-srv:base-val is deprecated.  Use svg_ros-srv:base instead.")
  (base m))

(cl:ensure-generic-function 'invert-val :lambda-list '(m))
(cl:defmethod invert-val ((m <EnvironmentSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader svg_ros-srv:invert-val is deprecated.  Use svg_ros-srv:invert instead.")
  (invert m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EnvironmentSrv-response>) ostream)
  "Serializes a message object of type '<EnvironmentSrv-response>"
  (cl:let* ((signed (cl:slot-value msg 'sensor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'light)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'base)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'invert)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EnvironmentSrv-response>) istream)
  "Deserializes a message object of type '<EnvironmentSrv-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sensor) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'light) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'base) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'invert) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EnvironmentSrv-response>)))
  "Returns string type for a service object of type '<EnvironmentSrv-response>"
  "svg_ros/EnvironmentSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EnvironmentSrv-response)))
  "Returns string type for a service object of type 'EnvironmentSrv-response"
  "svg_ros/EnvironmentSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EnvironmentSrv-response>)))
  "Returns md5sum for a message object of type '<EnvironmentSrv-response>"
  "caeffbf51b8bc21c7838947aa06fdc32")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EnvironmentSrv-response)))
  "Returns md5sum for a message object of type 'EnvironmentSrv-response"
  "caeffbf51b8bc21c7838947aa06fdc32")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EnvironmentSrv-response>)))
  "Returns full string definition for message of type '<EnvironmentSrv-response>"
  (cl:format cl:nil "int32 sensor~%int32 light~%int32 base~%int32 invert~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EnvironmentSrv-response)))
  "Returns full string definition for message of type 'EnvironmentSrv-response"
  (cl:format cl:nil "int32 sensor~%int32 light~%int32 base~%int32 invert~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EnvironmentSrv-response>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EnvironmentSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'EnvironmentSrv-response
    (cl:cons ':sensor (sensor msg))
    (cl:cons ':light (light msg))
    (cl:cons ':base (base msg))
    (cl:cons ':invert (invert msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'EnvironmentSrv)))
  'EnvironmentSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'EnvironmentSrv)))
  'EnvironmentSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EnvironmentSrv)))
  "Returns string type for a service object of type '<EnvironmentSrv>"
  "svg_ros/EnvironmentSrv")