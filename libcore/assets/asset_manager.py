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

from typing import Type, TypeVar, Any

from libcore.assets.loaders.bitmap_font_loader import BitmapFontLoader
from libcore.assets.loaders.resolvers.absolute_file_handle_resolver import AbsoluteFileHandleResolver
from libcore.assets.loaders.resolvers.ifile_handle_resolver import IFileHandleResolver
from libcore.graphics.g2d.bitmap_font import BitmapFont
from libcore.utils.Logger import Logger

T = TypeVar('T')

class AssetManager:

    _asset_dependencies: dict
    _assets: dict
    _asset_types: dict
    _injected: []
    _loaders: dict
    _load_queue: []
    _task_stack: []

    _exector: AsyncExecutor
    _listener: IAssetErrorListener
    _file_handle_resolver: IFileHandleResolver

    _loaded: int
    _peak_tasks: int
    _to_load: int

    logger: Logger

    def default_init(self,
                     resolver: IFileHandleResolver = AbsoluteFileHandleResolver.__new__,
                     default_loaders: bool = True):
        """
        Initialise this AssetManager using the supplied IFileHandleResolver.

        :param resolver: The resolver to use.
        :param default_loaders: Use default loaders if true.
        """
        logger = Logger()

        if default_loaders:
            self.set_loader(BitmapFont, BitmapFontLoader(resolver))
            self.set_loader(Music, MusicLoader(resolver))
            self.set_loader(Pixmap, PixmapLoader(resolver))
            self.set_loader(Sound, SoundLoader(resolver))
            self.set_loader(TextureAtlas, TextureAtlasLoader(resolver))
            self.set_loader(Texture, TextureLoader(resolver))
            self.set_loader(Skin, SkinLoader(resolver))
            self.set_loader(ParticleEffect, ParticleEffectLoader(resolver))

    def get(self, name: string, type: Type[T]) -> T:
        """
        Retrieves an asset of the specified type by its name.
        :param name: The name of the asset.
        :param type: The type of the asset.
        :return: The required asset.
        """
        pass

    def set_loader(self, typ, loader):
        pass

    def set_ref_count(self, fn: string, rc: int):
        """

        :param fn:
        :param rc:
        :return:
        """
        pass

    @property
    def loaded_assets_count(self):
        """
        :return: The number of currently loaded assets.
        """
        return len(self._asset_types)

    def clear(self):
        pass
