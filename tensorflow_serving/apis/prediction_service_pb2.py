# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/apis/prediction_service.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from tensorflow_serving.apis import predict_pb2 as third__party_dot_tensorflow__serving_dot_apis_dot_predict__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='tensorflow_serving/apis/prediction_service.proto',
    package='tensorflow.serving',
    syntax='proto3',
    serialized_pb=_b(
        '\n<tensorflow_serving/apis/prediction_service.proto\x12\x12tensorflow.serving\x1a\x31tensorflow_serving/apis/predict.proto2g\n\x11PredictionService\x12R\n\x07Predict\x12\".tensorflow.serving.PredictRequest\x1a#.tensorflow.serving.PredictResponseB\x03\xf8\x01\x01\x62\x06proto3'),
    dependencies=[
        third__party_dot_tensorflow__serving_dot_apis_dot_predict__pb2.
        DESCRIPTOR,
    ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(),
                                                _b('\370\001\001'))
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class BetaPredictionServiceServicer(object):
  """PredictionService provides basic machine learning methods.

  TODO(b/28599843): Decide whether to keep the separate services in addition to
  this combined service.
  """

  def Predict(self, request, context):
    """Predict.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaPredictionServiceStub(object):
  """PredictionService provides basic machine learning methods.

  TODO(b/28599843): Decide whether to keep the separate services in addition to
  this combined service.
  """

  def Predict(self,
              request,
              timeout,
              metadata=None,
              with_call=False,
              protocol_options=None):
    """Predict.
    """
    raise NotImplementedError()

  Predict.future = None


def beta_create_PredictionService_server(servicer,
                                         pool=None,
                                         pool_size=None,
                                         default_timeout=None,
                                         maximum_timeout=None):
  request_deserializers = {
      ('tensorflow.serving.PredictionService', 'Predict'):
          third__party_dot_tensorflow__serving_dot_apis_dot_predict__pb2.
          PredictRequest.FromString,
  }
  response_serializers = {
      ('tensorflow.serving.PredictionService', 'Predict'):
          third__party_dot_tensorflow__serving_dot_apis_dot_predict__pb2.
          PredictResponse.SerializeToString,
  }
  method_implementations = {
      ('tensorflow.serving.PredictionService', 'Predict'):
          face_utilities.unary_unary_inline(servicer.Predict),
  }
  server_options = beta_implementations.server_options(
      request_deserializers=request_deserializers,
      response_serializers=response_serializers,
      thread_pool=pool,
      thread_pool_size=pool_size,
      default_timeout=default_timeout,
      maximum_timeout=maximum_timeout)
  return beta_implementations.server(
      method_implementations, options=server_options)


def beta_create_PredictionService_stub(channel,
                                       host=None,
                                       metadata_transformer=None,
                                       pool=None,
                                       pool_size=None):
  request_serializers = {
      ('tensorflow.serving.PredictionService', 'Predict'):
          third__party_dot_tensorflow__serving_dot_apis_dot_predict__pb2.
          PredictRequest.SerializeToString,
  }
  response_deserializers = {
      ('tensorflow.serving.PredictionService', 'Predict'):
          third__party_dot_tensorflow__serving_dot_apis_dot_predict__pb2.
          PredictResponse.FromString,
  }
  cardinalities = {'Predict': cardinality.Cardinality.UNARY_UNARY,}
  stub_options = beta_implementations.stub_options(
      host=host,
      metadata_transformer=metadata_transformer,
      request_serializers=request_serializers,
      response_deserializers=response_deserializers,
      thread_pool=pool,
      thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(
      channel,
      'tensorflow.serving.PredictionService',
      cardinalities,
      options=stub_options)
# @@protoc_insertion_point(module_scope)