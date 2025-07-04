# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: remote_snake.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'remote_snake.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12remote_snake.proto\x12\tsnake_sim\"\x1d\n\x05\x43oord\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"\x15\n\x07SnakeId\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1d\n\x0bStartLength\x12\x0e\n\x06length\x18\x01 \x01(\x05\"9\n\rStartPosition\x12(\n\x0estart_position\x18\x01 \x01(\x0b\x32\x10.snake_sim.Coord\"\x96\x03\n\x0b\x45nvInitData\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x12\n\nfree_value\x18\x03 \x01(\x05\x12\x15\n\rblocked_value\x18\x04 \x01(\x05\x12\x12\n\nfood_value\x18\x05 \x01(\x05\x12=\n\x0csnake_values\x18\x06 \x03(\x0b\x32\'.snake_sim.EnvInitData.SnakeValuesEntry\x12\x43\n\x0fstart_positions\x18\x07 \x03(\x0b\x32*.snake_sim.EnvInitData.StartPositionsEntry\x12\x10\n\x08\x62\x61se_map\x18\x08 \x01(\x0c\x1aJ\n\x10SnakeValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.snake_sim.SnakeValues:\x02\x38\x01\x1aG\n\x13StartPositionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.snake_sim.Coord:\x02\x38\x01\"5\n\x0bSnakeValues\x12\x12\n\nhead_value\x18\x01 \x01(\x05\x12\x12\n\nbody_value\x18\x02 \x01(\x05\"\x8a\x01\n\x07\x45nvData\x12\x0b\n\x03map\x18\x01 \x01(\x0c\x12.\n\x06snakes\x18\x02 \x03(\x0b\x32\x1e.snake_sim.EnvData.SnakesEntry\x1a\x42\n\x0bSnakesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.snake_sim.SnakeRep:\x02\x38\x01\",\n\x08SnakeRep\x12\x10\n\x08is_alive\x18\x01 \x01(\x08\x12\x0e\n\x06length\x18\x02 \x01(\x05\"5\n\x0eUpdateResponse\x12#\n\tdirection\x18\x01 \x01(\x0b\x32\x10.snake_sim.Coord\"\x07\n\x05\x45mpty2\xae\x02\n\x0bRemoteSnake\x12-\n\x05SetId\x12\x12.snake_sim.SnakeId\x1a\x10.snake_sim.Empty\x12:\n\x0eSetStartLength\x12\x16.snake_sim.StartLength\x1a\x10.snake_sim.Empty\x12>\n\x10SetStartPosition\x12\x18.snake_sim.StartPosition\x1a\x10.snake_sim.Empty\x12\x37\n\x0bSetInitData\x12\x16.snake_sim.EnvInitData\x1a\x10.snake_sim.Empty\x12;\n\x06Update\x12\x12.snake_sim.EnvData\x1a\x19.snake_sim.UpdateResponse(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'remote_snake_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENVINITDATA_SNAKEVALUESENTRY']._loaded_options = None
  _globals['_ENVINITDATA_SNAKEVALUESENTRY']._serialized_options = b'8\001'
  _globals['_ENVINITDATA_STARTPOSITIONSENTRY']._loaded_options = None
  _globals['_ENVINITDATA_STARTPOSITIONSENTRY']._serialized_options = b'8\001'
  _globals['_ENVDATA_SNAKESENTRY']._loaded_options = None
  _globals['_ENVDATA_SNAKESENTRY']._serialized_options = b'8\001'
  _globals['_COORD']._serialized_start=33
  _globals['_COORD']._serialized_end=62
  _globals['_SNAKEID']._serialized_start=64
  _globals['_SNAKEID']._serialized_end=85
  _globals['_STARTLENGTH']._serialized_start=87
  _globals['_STARTLENGTH']._serialized_end=116
  _globals['_STARTPOSITION']._serialized_start=118
  _globals['_STARTPOSITION']._serialized_end=175
  _globals['_ENVINITDATA']._serialized_start=178
  _globals['_ENVINITDATA']._serialized_end=584
  _globals['_ENVINITDATA_SNAKEVALUESENTRY']._serialized_start=437
  _globals['_ENVINITDATA_SNAKEVALUESENTRY']._serialized_end=511
  _globals['_ENVINITDATA_STARTPOSITIONSENTRY']._serialized_start=513
  _globals['_ENVINITDATA_STARTPOSITIONSENTRY']._serialized_end=584
  _globals['_SNAKEVALUES']._serialized_start=586
  _globals['_SNAKEVALUES']._serialized_end=639
  _globals['_ENVDATA']._serialized_start=642
  _globals['_ENVDATA']._serialized_end=780
  _globals['_ENVDATA_SNAKESENTRY']._serialized_start=714
  _globals['_ENVDATA_SNAKESENTRY']._serialized_end=780
  _globals['_SNAKEREP']._serialized_start=782
  _globals['_SNAKEREP']._serialized_end=826
  _globals['_UPDATERESPONSE']._serialized_start=828
  _globals['_UPDATERESPONSE']._serialized_end=881
  _globals['_EMPTY']._serialized_start=883
  _globals['_EMPTY']._serialized_end=890
  _globals['_REMOTESNAKE']._serialized_start=893
  _globals['_REMOTESNAKE']._serialized_end=1195
# @@protoc_insertion_point(module_scope)
