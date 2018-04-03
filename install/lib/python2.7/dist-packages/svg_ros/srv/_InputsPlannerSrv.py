# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from svg_ros/InputsPlannerSrvRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class InputsPlannerSrvRequest(genpy.Message):
  _md5sum = "3c2bcf2ff0894cb3058b1bf4c8c4175a"
  _type = "svg_ros/InputsPlannerSrvRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 success
"""
  __slots__ = ['success']
  _slot_types = ['int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InputsPlannerSrvRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = 0
    else:
      self.success = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_i.pack(self.success))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (self.success,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_i.pack(self.success))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.success,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from svg_ros/InputsPlannerSrvResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class InputsPlannerSrvResponse(genpy.Message):
  _md5sum = "8f16552e1a74db709956ba597f0eadc7"
  _type = "svg_ros/InputsPlannerSrvResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 origin_x
float64 origin_y
float64 origin_angRob
float64 dest_x
float64 dest_y
string sensorBool
int32 num_sensorsInt
float64 angle_sensor_orig
float64 range_angleRob
float64 radiusRob
float64 advance
float64 max_angle
int32 num_steps
int32 select
float64 largest_sensor
string pathNAme
string fileNAme
int32 flgGUI
int32 flg_noise

"""
  __slots__ = ['origin_x','origin_y','origin_angRob','dest_x','dest_y','sensorBool','num_sensorsInt','angle_sensor_orig','range_angleRob','radiusRob','advance','max_angle','num_steps','select','largest_sensor','pathNAme','fileNAme','flgGUI','flg_noise']
  _slot_types = ['float64','float64','float64','float64','float64','string','int32','float64','float64','float64','float64','float64','int32','int32','float64','string','string','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       origin_x,origin_y,origin_angRob,dest_x,dest_y,sensorBool,num_sensorsInt,angle_sensor_orig,range_angleRob,radiusRob,advance,max_angle,num_steps,select,largest_sensor,pathNAme,fileNAme,flgGUI,flg_noise

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InputsPlannerSrvResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.origin_x is None:
        self.origin_x = 0.
      if self.origin_y is None:
        self.origin_y = 0.
      if self.origin_angRob is None:
        self.origin_angRob = 0.
      if self.dest_x is None:
        self.dest_x = 0.
      if self.dest_y is None:
        self.dest_y = 0.
      if self.sensorBool is None:
        self.sensorBool = ''
      if self.num_sensorsInt is None:
        self.num_sensorsInt = 0
      if self.angle_sensor_orig is None:
        self.angle_sensor_orig = 0.
      if self.range_angleRob is None:
        self.range_angleRob = 0.
      if self.radiusRob is None:
        self.radiusRob = 0.
      if self.advance is None:
        self.advance = 0.
      if self.max_angle is None:
        self.max_angle = 0.
      if self.num_steps is None:
        self.num_steps = 0
      if self.select is None:
        self.select = 0
      if self.largest_sensor is None:
        self.largest_sensor = 0.
      if self.pathNAme is None:
        self.pathNAme = ''
      if self.fileNAme is None:
        self.fileNAme = ''
      if self.flgGUI is None:
        self.flgGUI = 0
      if self.flg_noise is None:
        self.flg_noise = 0
    else:
      self.origin_x = 0.
      self.origin_y = 0.
      self.origin_angRob = 0.
      self.dest_x = 0.
      self.dest_y = 0.
      self.sensorBool = ''
      self.num_sensorsInt = 0
      self.angle_sensor_orig = 0.
      self.range_angleRob = 0.
      self.radiusRob = 0.
      self.advance = 0.
      self.max_angle = 0.
      self.num_steps = 0
      self.select = 0
      self.largest_sensor = 0.
      self.pathNAme = ''
      self.fileNAme = ''
      self.flgGUI = 0
      self.flg_noise = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_5d.pack(_x.origin_x, _x.origin_y, _x.origin_angRob, _x.dest_x, _x.dest_y))
      _x = self.sensorBool
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_i5d2id.pack(_x.num_sensorsInt, _x.angle_sensor_orig, _x.range_angleRob, _x.radiusRob, _x.advance, _x.max_angle, _x.num_steps, _x.select, _x.largest_sensor))
      _x = self.pathNAme
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.fileNAme
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.flgGUI, _x.flg_noise))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.origin_x, _x.origin_y, _x.origin_angRob, _x.dest_x, _x.dest_y,) = _struct_5d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.sensorBool = str[start:end].decode('utf-8')
      else:
        self.sensorBool = str[start:end]
      _x = self
      start = end
      end += 60
      (_x.num_sensorsInt, _x.angle_sensor_orig, _x.range_angleRob, _x.radiusRob, _x.advance, _x.max_angle, _x.num_steps, _x.select, _x.largest_sensor,) = _struct_i5d2id.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pathNAme = str[start:end].decode('utf-8')
      else:
        self.pathNAme = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.fileNAme = str[start:end].decode('utf-8')
      else:
        self.fileNAme = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.flgGUI, _x.flg_noise,) = _struct_2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_5d.pack(_x.origin_x, _x.origin_y, _x.origin_angRob, _x.dest_x, _x.dest_y))
      _x = self.sensorBool
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_i5d2id.pack(_x.num_sensorsInt, _x.angle_sensor_orig, _x.range_angleRob, _x.radiusRob, _x.advance, _x.max_angle, _x.num_steps, _x.select, _x.largest_sensor))
      _x = self.pathNAme
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.fileNAme
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.flgGUI, _x.flg_noise))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.origin_x, _x.origin_y, _x.origin_angRob, _x.dest_x, _x.dest_y,) = _struct_5d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.sensorBool = str[start:end].decode('utf-8')
      else:
        self.sensorBool = str[start:end]
      _x = self
      start = end
      end += 60
      (_x.num_sensorsInt, _x.angle_sensor_orig, _x.range_angleRob, _x.radiusRob, _x.advance, _x.max_angle, _x.num_steps, _x.select, _x.largest_sensor,) = _struct_i5d2id.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pathNAme = str[start:end].decode('utf-8')
      else:
        self.pathNAme = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.fileNAme = str[start:end].decode('utf-8')
      else:
        self.fileNAme = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.flgGUI, _x.flg_noise,) = _struct_2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_5d = struct.Struct("<5d")
_struct_2i = struct.Struct("<2i")
_struct_i5d2id = struct.Struct("<i5d2id")
class InputsPlannerSrv(object):
  _type          = 'svg_ros/InputsPlannerSrv'
  _md5sum = '188578d1209fb9d01aa3d1efc9744987'
  _request_class  = InputsPlannerSrvRequest
  _response_class = InputsPlannerSrvResponse
