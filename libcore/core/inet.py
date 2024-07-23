# ///////////////////////////////////////////////////////////////////////////////
# Copyright [2023] [Richard Ikin]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ///////////////////////////////////////////////////////////////////////////////
import string
from abc import ABC, abstractmethod
from enum import Enum


class INet( ABC ):

    class IHttpResponse( ABC ):

        @abstractmethod
        def get_result( self ) -> [ ]:
            pass

        @abstractmethod
        def get_result_as_string( self ) -> string:
            pass

        @abstractmethod
        def get_result_as_stream( self ) -> StreamReader:
            pass

        @abstractmethod
        def get_status( self ) -> HttpStatus:
            pass

        @abstractmethod
        def get_header( self ) -> string:
            pass

        @abstractmethod
        def get_headers( self ) -> dict:
            pass

        Dictionary < string, List < string > > GetHeaders();
        pass

    class IHttpMethods( ABC ):
        pass

    class IHttpResponseListener( ABC ):
        pass

    class Protocol( Enum ):
        pass

    class HttpRequest( ABC ):
        pass
