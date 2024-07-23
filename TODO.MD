Python 2D Game Framework heavily inspired by the Java LibGDX Game Framework.

It is NOT a 100% conversion, some things may be different.

TODO List is below.

MAJOR OBSTACLES SO FAR:-

    - File Handling / Differences with Java
    - Listener / Observer pattern implementations

The standard of the code here won't be great to start off with, but will hopefully improve as I
learn more about Python.

Project name is to change. Current candidates are:-

    - LughEngine
    - Lugh
    - LughGDX
    - PYGDX

As far as I can see, I do not need to convert:-

    - Regex
    - Reflection
    - Concurrent ( AtomicInteger, AtomicQueue etc )
    - Async?
    - Network
    - Compression?

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

LIBGDX Python CONVERSION - ROUND 1
----------------------------------

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- STEP 1: Complete all conversions so that the code will build.
- STEP 2: Refactor, where possible and necessary, to take advantage of Python language features.
-         Some classes can become structs / records instead.
-         Some/Most Get / Set method declarations in interfaces could become Properties.
-         switch expressions instead of switch statements where appropriate.
-         switch expressions instead of if..if/else..else where appropriate.
-         Check methods to see if they can be virtual.
-         Use sealed classes only where strictly necessary. Users should be able to extend library classes.
-         Use of virtual for base classes/methods and classes that are likely to be extended is essential.
- STEP 3: Resolve ALL remaining TODOs.
- STEP 4: Ensure code is fully documented.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- NO MAGIC NUMBERS!!!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- SORT OUT VERSIONING!!!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- IP = Conversion In Progress.
- DONE = Class finished but may not be fully 'Python-ified'

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- PRIORITY is 2D classes first

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- Constantly look for opportunities to improve this code.
- There seems to be different namings for width/height etc properties and methods. Make it more uniform
- Make more use of <inheritdoc cref=""/>> or just <inheritdoc/>
-

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

ASSETS
------

    - DONE - AssetDescriptor
    - DONE - AssetLoaderParameters
    -      - AssetLoadingTask
    -      - AssetManager
    -      - IAssetErrorListener
    -      - RefCountedContainer

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

ASSETS/LOADERS
--------------

    -      - AssetLoader
    -      - AsynchronousAssetLoader
    -      - BitmapFontLoader
    -      - CubemapLoader
    -      - ModelLoader
    -      - MusicLoader
    -      - ParticleEffectLoader
    -      - PixmapLoader
    -      - ShaderProgramLoader
    -      - SkinLoader
    -      - SoundLoader
    -      - SynchronousAssetLoader
    -      - TextureAtlasLoader
    -      - TextureLoader

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

ASSETS/LOADERS/RESOLVERS
------------------------

    -      - AbsoluteFileHandleResolver
    -      - ClasspathFileHandleResolver
    -      - ExternalFileHandleResolver
    -      - IFileHandleResolver
    -      - InternalFileHandleResolver
    -      - LocalFileHandleResolver
    -      - PrefixFileHandleResolver
    -      - ResolutionFileResolver

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

AUDIO
-----

    -      - IAudioDevice
    -      - IAudioRecorder
    -      - IMusic
    -      - ISound

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

AUDIO/MP3SHARP
--------------

    -      - Buffer16BitSterso
    -      - MP3SharpException
    -      - MP3Stream
    -      - SoundFormat

    Decoding
    --------

    -      - AudioBase
    -      - BitReserve
    -      - Bitstream
    -      - BitstreamErrors
    -      - BitstreamException
    -      - CircularByteBuffer
    -      - Crc16
    -      - Decoder
    -      - Decode.Parameters
    -      - DecoderErrors
    -      - DecoderException
    -      - Equalizer
    -      - Header
    -      - Huffman
    -      - OuputChannels
    -      - OutputChannelsEnum
    -      - PushbackStream
    -      - SampleBuffer
    -      - SynthesisFilter

    Decoders
    --------

    -      - ASubband
    -      - IFrameDecoder
    -      - LayerIDecoder
    -      - LayerIIDecoder
    -      - LayerIIIDecoder

    Decoders/LayerI
    ---------------

    -      - SubbandLayer1
    -      - SubbandLayer1IntensityStereo
    -      - SubbandLayer1Stereo

    Decoders/LayerII
    ----------------

    -      - SubbandLayer2
    -      - SubbandLayer2IntensityStereo
    -      - SubbandLayer2Stereo

    Decoders/LayerIII
    -----------------

    -      - ChannelData
    -      - GranuleInfo
    -      - Layer3SideInfo
    -      - SBI
    -      - ScaleFactorData
    -      - ScaleFactorTable

    IO
    --

    -      - RandomAccessFileStream
    -      - RiffFile
    -      - WaveFile
    -      - WaveFileBuffer

    Support
    -------

    -      - SupportClass

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

AUDIO/OPENAL
------------

    -      - AL
    -      - ALC

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

CORE
----

    - DONE - AbstractGraphics
    - DONE - AbstractInput
    - DONE - ApplicationAdapter
    - DONE - Game
    - DONE - Gdx
    - DONE - GDXVersion
    - DONE - IApplication
    - DONE - IApplicationListener
    - DONE - IApplicationLogger
    - DONE - IAudio
    - DONE - IFile
    -      - IGraphics
    -      - IGraphics.DisplayModeDescriptor
    -      - IGraphics.MonitorDescriptor
    -      - IGraphics.BufferFormatDescriptor
    -      - IInput
    -      - IInput.Buttons
    -      - IInput.Keys
    -      - IInput.ITextInputListener
    -      - IInputProcessor                
    -      - ILifecycleListener             
    -      - INet
    -      - INet.IHttpResponse
    -      - INet.IHttpMethods
    -      - INet.IHttpResponseListener
    -      - INet.HttpRequest
    -      - InputAdapter                   
    -      - InputEventQueue                
    -      - IPreferences                   
    -      - IScreen                        
    -      - ScreenAdapter                  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FILES - DELETE CANDIDATE
------------------------

    TODO: Remove all this and properly integrate the Python file handling classes

    -      - BufferedStreamExtensions
    -      - ByteArrayInputStream
    -      - FileHandle
    -      - InputStream

    ------------------------------------------
    - java.io.BufferedReader                -> 
    - java.io.BufferedInputStream           -> BufferedStream ?
    - java.io.ByteArrayInputStream          -> 
    - java.io.ByteArrayOutputStream         -> 
    - java.io.DataInputStream               -> BinaryReader ?
    - java.io.DataOutputStream              -> BinaryWriter ?
    - java.io.File                          -> File ( static class )
    - java.io.FileHandle                    -> FileInfo + File + DirectoryInfo ?
    - java.io.FileInputStream               -> 
    - java.io.FileOutputStream              -> 
    - java.io.FilterInputStream             -> 
    - java.io.FilterOutputStream            -> 
    - java.io.DataOuput                     -> (Interface)
    - java.io.InputStream                   -> StreamReader ?
    - java.io.InputStreamReader             -> StreamReader ?
    - java.io.IOException                   -> System.IO.IOException
    - java.io.OutputStream                  -> StreamWriter ?
    - java.io.Reader                        -> StreamReader ?

    ------------------------------------------

    - Look into existing Python ZIP libraries

    - java.util.zip.CRC32                   -> 
    - java.util.zip.CheckedOutputStream     -> 
    - java.util.zip.Deflater                -> 
    - java.util.zip.DeflaterOutputStream    -> 
    - java.util.zip.InflaterInputStream     -> 

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FILES/BUFFERS - DELETE CANDIDATE
--------------------------------

    - See if these can be replaced by any Python System classes

    -      - Buffer
    -      - BufferUtils
    -      - ByteBuffer
    -      - CharBuffer
    -      - CircularByteBuffer
    -      - DirectByteBuffer
    -      - DoubleBuffer
    -      - FloatBuffer
    -      - HeapByteBuffer
    -      - HeapCharBuffer
    -      - HeapFloatBuffer
    -      - HeapShortBuffer
    -      - IDirectBuffer
    -      - IntBuffer
    -      - LongBuffer
    -      - MappedByteBuffer
    -      - ShortBuffer
    -      - StringCharBuffer

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS
--------

    -      - Camera                             
    -      - Color                              
    -      - Colors                             
    -      - Cubemap
    -      - FPSLogger                          
    -      - GLTexture                          
    -      - GraphicsType                       
    -      - ICubemapData                       
    -      - ICursor                            
    -      - IDownloadPixmapResponseListener    
    -      - IGL20                              
    -      - IGL30                              
    -      - ITextureArrayData        
    -      - ITextureData             
    -      - Mesh                               
    -      - OrthographicCamera                 
    -      - PerspectiveCamera                  
    -      - Pixmap              
    -      - PixmapFormat                             
    -      - PixmapIO
    -      - Texture                            
    -      - TextureArray                       
    -      - TextureFilter                      
    -      - TextureWrap                        
    -      - VertexAttribute                    
    -      - VertexAttributes

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/FRAMEBUFFERS
---------------------

    -      - FloatFrameBuffer
    -      - FloatFrameBufferBuilder
    -      - FrameBuffer
    -      - FrameBufferBuilder
    -      - FrameBufferCubemap
    -      - FrameBufferCubemapBuilder
    -      - FrameBufferRenderBufferAttachmentSpec
    -      - FrameBufferTextureAttachmentSpec
    -      - GLFrameBuffer
    -      - GLFrameBufferBuilder

    ** Restructure GLFrameBuffer.Build(), this method is too long.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G2D
------------

    -      - Animation                      
    -      - AtlasRegion                    
    -      - AtlasSprite                    
    -      - BitmapFont 
    -      - BitmapFontCache                
    -      - CpuSpriteBatch                 
    -      - DistanceFieldFont              
    -      - Gdx2DPixmap                    
    -      - GlyphLayout                    
    -      - IBatch                         
    -      - IPolygonBatch                  
    -      - NinePatch                      
    -      - ParticleEffect                 
    -      - ParticleEffectPool        
    -      - ParticleEmitter           
    -      - PixmapPacker
    -      - PixmapPacker10       
    -      - PolygonRegion                  
    -      - PolygonRegionLoader
    -      - PolygonSprite                  
    -      - PolygonSpriteBatch             
    -      - RepeatablePolygonSprite        
    -      - Sprite                         
    -      - SpriteBatch                    
    -      - SpriteCache
    -      - TextureAtlas                   
    -      - TextureAtlasData   
    -      - TextureAtlasDataExtensions
    -      - TextureRegion                  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D
------------

    -      - Attribute
    -      - AttributesGroup
    -      - Environment
    -      - Material
    -      - Model
    -      - ModelBatch
    -      - ModelCache
    -      - ModelInstance
    -      - Renderable
    -      - RenderableProvider
    -      - Shader

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/ATTRIBUTES
-----------------------

    -      - BlendingAttribute
    -      - ColorAttribute
    -      - CubemapAttribute
    -      - DepthTestAttribute
    -      - DirectionalLightsAttribute
    -      - FloatAttribute
    -      - IntAttribute
    -      - PointLightsAttribute
    -      - SpotLightsAttribute
    -      - TextureAttribute

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/DECALS
-------------------

    -      - CameraGroupStrategy
    -      - Decal
    -      - DecalBatch
    -      - DecalMaterial
    -      - IGroupPlug
    -      - IGroupStrategy
    -      - PluggableGroupStrategy
    -      - SimpleOrthoGroupStrategy

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/ENV
----------------

    -      - AmbientCubemap
    -      - BaseLight
    -      - DirectionalLight
    -      - DirectionalShadowLight
    -      - IShadowMap
    -      - PointLight
    -      - SpericalHarmonics
    -      - SpotLight

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/LOADER
-------------------

    -      - G3ModelLoader
    -      - ObjLoader

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/MODELS
-------------------

    -      - Attribute
    -      - MeshPart
    -      - Node
    -      - NodeAnimation
    -      - NodeKeyframe
    -      - NodePart

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/MODELS/DATA
------------------------

    -      - ModelAnimation
    -      - ModelData
    -      - ModelMaterial
    -      - ModelMesh
    -      - ModelMeshPart
    -      - ModelNode
    -      - ModelNodeAnimation
    -      - ModelNodeKeyframe
    -      - ModelNodePart
    -      - ModelTexture

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/PARTICLES
----------------------

    -      - ParallelArray
    -      - ParticleChannels
    -      - ParticleController
    -      - ParticleControllerComponent
    -      - ParticleEffect
    -      - ParticleEffectLoader
    -      - ParticleShader
    -      - ParticleSorter
    -      - ParticleSystem
    -      - ResourceData

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/PARTICLES/BATCHES
------------------------------

    -      - BillboardParticleBatch
    -      - BufferedParticleBatch
    -      - IParticleBatch
    -      - ModelInstanceParticleBatch
    -      - PointSpriteParticleBatch

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/PARTICLES/EMITTERS
-------------------------------

    -      - Emitter
    -      - RegulatEmitter

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/PARTICLES/INFLUENCERS
----------------------------------

    -      - ColorInfluencer
    -      - DynamicsInfluencer
    -      - DynamicsModifier
    -      - Influencer
    -      - ModelInfluencer
    -      - ParticleControllerFinalizerInfluencer
    -      - ParticleControllerInfluencer
    -      - RegionInfluencer
    -      - ScaleInfluencer
    -      - SimpleInfluencer
    -      - SpawnInfluencer

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/PARTICLES/RENDERERS
--------------------------------

    -      - BillboardControllerRenderData
    -      - BillboardRenderer
    -      - ModelInstanceControllerRenderData
    -      - ModelInstanceRenderer
    -      - ParticleControllerControllerRenderer
    -      - ParticleControllerRenderData
    -      - ParticleControllerRenderer
    -      - PointSpriteControllerRenderData
    -      - PointSpriteRenderer

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/PARTICLES/VALUES
-----------------------------

    -      - CylinderSpawnShapeValue
    -      - EllipseSpawnShapeValue
    -      - GradientColorValue
    -      - LineSpawnShapeValue
    -      - MeshSpawnShapeValue
    -      - NumericValue
    -      - ParticleValue
    -      - PointSpawnShapeValue
    -      - PrimitiveSpawnShapeValue
    -      - RangedNumericValue
    -      - RectangleSpawnShapeValue
    -      - ScaledNumericValue
    -      - SpawnShapeValue
    -      - UnweightedMeshSpawnShapeValue
    -      - WeightMeshSpawnShapeValue

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/SHADERS
--------------------

    -      - BaseShader
    -      - DefaultShader
    -      - DepthShader

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/UTILS
------------------

    -      - AnimationController
    -      - BaseAnimationController
    -      - BaseShaderProvider
    -      - CameraInputController
    -      - DefaultRenderableSorter
    -      - DefaultShaderProvider
    -      - DefaultTextureBinder
    -      - DepthShaderProvider
    -      - F|irstPersonCameraController
    -      - IMeshPartBuilder
    -      - IRenderableSorter
    -      - IShaderProvider
    -      - ITextureBinder
    -      - ITextureProvider
    -      - MeshBuilder
    -      - ModelBuilder
    -      - RenderContext
    -      - ShapeCache
    -      - TextureDescriptor

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/G3D/UTILS/SHAPEBUILDERS
--------------------------------

    -      - ArrowShapeBuilder
    -      - BaseShapeBuilder
    -      - BoxShapeBuilder
    -      - CapsuleShapeBuilder
    -      - ConeShapeBuilder
    -      - CylinderShapeBuilder
    -      - EllipseShapeBuilder
    -      - FrustrumShapeBuilder
    -      - PatchShapeBuilder
    -      - RenderableShapeBuilder
    -      - SphereShapeBuilder

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/GLUTILS
----------------

    -      - FacedCubemapData
    -      - FileTextureArrayData
    -      - FileTextureData
    -      - FloatTextureData
    -      - GLOnlyTextureData
    -      - GLVersion
    -      - HdpiMode
    -      - HdpiUtils
    -      - IImmediateModeRenderer
    -      - IIndexData
    -      - IInstanceData
    -      - ImmediateModeRenderer20
    -      - IndexArray
    -      - IndexBufferObject
    -      - IndexBufferObjectSubData
    -      - InstanceBufferObject
    -      - InstanceBufferObjectSubData
    -      - IVertexData
    -      - KTXTTextureData
    -      - MipMapGenerator
    -      - MipMapTextureData
    -      - PixmapTextureData
    -      - ShaderProgram
    -      - ShapeRenderer

        The following classes have a lot in common.
        Perhaps create a base class they all extend from?

    -      - VertexArray
    -      - VertexBufferObject
    -      - VertexBufferObjectSubData
    -      - VertexBufferObjectWithVAO

    - The following do not need converting

    - **** - ETC1
    - **** - ETC1TextureData

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/PROFILING
------------------

    -      - GL20Interceptor
    -      - GL30Interceptor
    -      - GLInterceptor
    -      - GLProfiler
    -      - IGLErrorListener

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

INPUT
-----

    - Not sure about these. Am I supporting mobile? Probably?

    -      - GestureDetector
    -      - RemoteInput
    -      - RemoteSender

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

MAPS
----

    -      - IImageResolver                         
    -      - IMapRenderer                           
    -      - Map                                    
    -      - MapGroupLayer                          
    -      - MapLayer                               
    -      - MapLayers                              
    -      - MapObject                              
    -      - MapObjects                             
    -      - MapProperties                          

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

MAPS/OBJECTS
------------

    -      - CircleMapObject                        
    -      - EllipseMapObject                       
    -      - PolygonMapObject                       
    -      - PolylineMapObject                      
    -      - RectangleMapObject                     
    -      - TextureMapObject                       

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

MAPS/TILED
----------

    -      - ITiledMapTile                          
    -      - TiledMap                               
    -      - TiledMapImageLayer                     
    -      - TiledMapTileLayer                      
    -      - TiledMapTileSet                        
    -      - TiledMapTileSets                       

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

MAPS/TILED/LOADERS
------------------

    -      - AtlasTmxMapLoader 
    -      - BaseTmxMapLoader
    -      - TmxMapLoader
    - **** - TideMapLoader

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

MAPS/TILED/OBJECTS
------------------

    -      - TiledMapTileMapObject                  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

MAPS/TILED/RENDERERS
--------------------

    -      - BatchTiledMapRenderer                  
    -      - HexagonalTiledMapRenderer              
    -      - IsometricStaggeredTiledMapRenderer     
    -      - IsometricTiledMapRenderer              
    -      - ITiledMapRenderer                      
    -      - OrthoCachedTiledMapRenderer            
    -      - OrthogonalTiledMapRenderer             

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

MAPS/TILED/TILES
----------------

    -      - AnimatedTileMapTile                    
    -      - StaticTiledMapTile                     

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

MATHS
-----

    -      - Affine2
    -      - Bezier
    -      - Bresenham2
    -      - BSpline
    -      - CatmullRomSpline
    -      - Circle
    -      - ConvexHull
    -      - CumulativeDistribution
    -      - DelaunayTriangulator
    -      - EarClippingTriangulator
    -      - Ellipse
    -      - FloatConsts
    -      - FloatCounter
    -      - Frustrum
    -      - GeometryUtils
    -      - GridPoint2
    -      - GridPoint3
    -      - Interpolation
    -      - Intersector
    -      - IPath
    -      - IShape2D
    -      - IVector
    -      - MathUtils
    -      - Matrix3                        
    -      - Matrix4                        
    -      - Number
    -      - NumberUtils                    
    -      - Plane
    -      - Polygon
    -      - Polyline
    -      - Quaternion
    -      - RandomXS128
    -      - RectangleShape
    -      - Vector2                        Convert, I prefer the way the LibGDX class works.
    -      - Vector3                        Convert, I prefer the way the LibGDX class works.
    -      - WindowedMean

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

MATH/COLLISION
--------------

    -      - BoundingBox
    -      - Ray
    -      - Segment
    -      - Sphere

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

NETWORK - DELETE CANDIDATE
-------

    Note:- All this is probably already supported by Python System

    - **** - HttpParametersUtils
    - **** - HttpRequestBuilder
    - **** - HttpStatus
    - **** - IHttpRequestHeader
    - **** - IHttpResponseHeader
    - **** - IServerSocket
    - **** - ISocket
    - **** - NetJavaImpl
    - **** - NetJavaServerSocketImpl
    - **** - NetJavaSocketImpl
    - **** - ServerSocketHints
    - **** - SocketHints

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

SCENES/SCENE2D
--------------

    -      - Action
    -      - Actor
    -      - Event
    -      - Group
    -      - IActor
    -      - InputEvent
    -      - Stage
    -      - Touchable
    -      - TouchFocus

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

SCENES/SCENE2D/ACTIONS
----------------------

    -      - Actions                        
    -      - AddAction                      
    -      - AddListenerAction              
    -      - AfterAction                    
    -      - AlphaAction                    
    -      - ColorAction                    
    -      - CountdownEventAction           
    -      - DelayAction                    
    -      - DelegateAction                 
    -      - EventAction                    
    -      - FloatAction                    
    -      - IntAction                      
    -      - LayoutAction                   
    -      - MoveByAction                   
    -      - MoveToAction                   
    -      - ParallelAction                 
    -      - RelativeTemporalAction         
    -      - RemoveAction                   
    -      - RemoveActorAction              
    -      - RemoveListenerAction           
    -      - RepeatAction                   
    -      - RotateByAction                 
    -      - RotateToAction                 
    -      - RunnableAction                 
    -      - ScaleByAction                  
    -      - ScaleToAction                  
    -      - SequenceAction                 
    -      - SizeByAction                   
    -      - SizeToAction                   
    -      - TemporalAction                 
    -      - TimeScaleAction                
    -      - TouchableAction                
    -      - VisibleAction                  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

SCENES/SCENE2D/LISTENERS
------------------------

    - Base classes to be used and extended as required

    -      - ActorGestureListener           
    -      - ChangeListener                 
    -      - ClickListener                  
    -      - DragListener                   
    -      - DragScrollListener             
    -      - FocusListener                  
    -      - IEventListener                 
    -      - InputListener                  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

SCENES/SCENE2D/UI
-----------------

    TODO: I don't like the way Cell and Value classes are implemented.
          They seem confusing and are candidates for a rewrite.

    -      - Button
    -      - ButtonGroup
    -      - Cell
    -      - CheckBox
    -      - Container
    -      - Dialog
    -      - DialogChangeListener
    -      - DialogFocusListener
    -      - DialogInputListener
    -      - HorizontalGroup
    -      - Image
    -      - ImageButton
    -      - ImageTextButton
    -      - Label
    -      - ListBox
    -      - ParticleEffectActor            
    -      - ProgressBar
    -      - ScrollPane
    -      - ScrollPaneListeners
    -      - SelectBox
    -      - Skin                           
    -      - Slider                         
    -      - SplitPane                      
    -      - Stack                          
    -      - Table                          
    -      - TextArea                       
    -      - TextButton
    -      - TextField      Check that _blinkTask and _KeyRepeatTask are disposed of properly                      
    -      - Tooltip
    -      - TextTooltip
    -      - TooltipManager                 
    -      - Touchpad                       
    -      - Tree
    -      - Value                          
    -      - ValueExtensions
    -      - VerticalGroup                  
    -      - Widget                         
    -      - WidgetGroup                    
    -      - Window                         

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

SCENES/SCENE2D/UTILS
--------------------

    -      - ArraySelection                 
    -      - BaseDrawable                   
    -      - DragAndDrop                    
    -      - ICullable                      
    -      - IDisableable                   
    -      - IDrawable                      
    -      - ILayout                        
    -      - ITransformDrawable             
    -      - NinePatchDrawable              
    -      - ScissorStack                   
    -      - Selection                      
    -      - SpriteDrawable                 
    -      - TextureRegionDrawable          
    -      - TiledDrawable                  
    -      - UIUtils                        

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS
-----

    -      - Align                          
    -      - BinaryHeap
    -      - Bits                           
    -      - Character
    -      - ComparableTimSort              
    -      - DataInput                      Check
    -      - DataOutput                     Check
    -      - DataUtils                      Added Class
    - DONE - ICloseable                     
    - DONE - IClipboard                     Convert - Interface, clipboard handled in backends.
    - DONE - IDisposable
    -      - IRunnable
    -      - Logger                         
    -      - PerformanceCounter             Check
    -      - PerformanceCounters            Check
    -      - PropertiesUtils                Convert, but check if necessary first
    -      - QuadTreeFloat
    -      - QuickSelect
    -      - Scaling
    -      - ScreenUtils
    -      - Select
    -      - SharedLibraryLoader
    -      - SharedLibraryLoader.SystemHelpers
    -      - SortUtils
    -      - StringTokenizer
    -      - Timer                          
    -      - TimeUtils
    -      - TimSort
    -      - Trace                          Addition

    - The following do not need converting

    - **** - Base64Coder
    - **** - GdxNativesLoader
    - **** - I18NBundle
    - **** - LittleEndianInputStream
    - **** - PauseableThread
    - **** - Queue
    - **** - SortedIntList
    - **** - StreamUtils
    - **** - StringBuilder
    - **** - TextFormatter

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/ASYNC - DELETE CANDIDATE
-----------

    - **** - AsyncExecutor
    - **** - ASyncResult
    - **** - IAsyncTask
    - **** - ThreadUtils

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/COLLECTIONS
-----------------

    -      - Array<T>                       Converted, but use List<T> for most cases.
    -      - CollectionsData
    -      - DelayedRemovalArray            Convert / Extend List<>
    -      - IdentityMap<K, V>              Convert / extend Dictionary< object, object > 
    -      - ObjectMap                      Converted, but use Dictionary< object, object >
    -      - PredicateIterable
    -      - PredicateIterator
    - IP   - SnapshotArray<T>

    ----------------------------------------------------------------------------------

    -      - DictionaryExtensions
    -      - ListExtensions

    ----------------------------------------------------------------------------------

    - The following do not need converting

    - **** - ArrayMap                       Use Dictionary<K, V>
    - **** - ArrayIterable                  Use IEnumerable?
    - **** - ArrayIterator                  Use IEnumerator?
    - **** - BoolArray                      Use List< bool >
    - **** - ByteArray                      Use List< byte >
    - **** - CharArray                      Use List< char >
    - **** - FloatArray                     Use List< float >
    - **** - IntArray                       Use List< int >
    - **** - IntFloatMap                    Use Dictionary< int, float >
    - **** - IntIntMap                      Use Dictionary< int, int >
    - **** - IntMap                         Use Dictionary< int, V >
    - **** - IntSet                         Use List<int>
    - **** - IPredicate                     ????
    - **** - LongArray                      Use List< long >
    - **** - LongMap                        Use Dictionary< long, V >
    - **** - ObjectFloatMap                 Use Dictionary< object, float >
    - **** - ObjectIntMap                   Use Dictionary< object, int >
    - **** - ObjectLongMap                  Use Dictionary< object, long >
    - **** - ObjectSet<T>                   Use List<T>
    - **** - OrderedMap<K, V>               Use SortedDictionary<K, V> ?
    - **** - OrderedSet<T>                  Use SortedSet<T>
    - **** - ShortArray                     Use List< short >

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/EXCEPTIONS
----------------

    These need more documentation!

    -      - AssetNotLoadedException        
    -      - BufferOverflowException        
    -      - BufferUnderflowException       
    -      - GdxRuntimeException            
    -      - IllegalStateException          
    -      - InvalidMarkException       
    -      - InvalidTypeException       
    -      - MemberNullException
    -      - MissingResourceException
    -      - NoSuchElementException         
    -      - NumberFormatException          
    -      - ReadOnlyBufferException        
    -      - UnsupportedEncodingException   
    -      - UnsupportedOperationException  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/POOLING
-------------

    -      - FlushablePool                  
    -      - IPoolable                      
    -      - Pool                           
    -      - PooledLinkedList               
    -      - Pools                          

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/VIEWPORT
--------------

    -      - ExtendedViewport               
    -      - FillViewport                   
    -      - FitViewport                    
    -      - ScalingViewport                
    -      - ScreenViewport                 
    -      - StretchViewport                
    -      - Viewport                       

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/XML
---------

    - TODO: Switch to System.Xml

    -      - XmlReader          Some 'unreachable code' fixes needed
    -      - XmlReaderData
    -      - XmlWriter

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

TESTS/CORE/GRAPHICS
-------------------

    -      - CameraTest

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

BACKENDS/DESKTOPGL
------------------

    -      - DesktopGLApplication
    -      - DesktopGLApplicationConfiguration
    -      - DesktopGLNativesLoader
    -      - DesktopGLNet
    -      - DesktopWindowCallbacks
    -      - IDesktopGLApplicationBase
    -      - Sync

    Files
    -----

    -      - DesktopGLFileHandle
    -      - DesktopGLFiles

    Graphics
    --------

    -      - DesktopGL20
    -      - DesktopGL30
    -      - DesktopGLGraphics
    -      - DesktopGLGraphics.DesktopGLDisplayMode   Delete candidate
    -      - DesktopGLGraphics.DesktopGLMonitor       Delete candidate

    Input
    -----

    -      - DefaultGLInput
    -      - IDesktopGLInput

    Utils
    -----

    -      - DesktopGLApplicationLogger
    -      - DesktopGLClipboard
    -      - DesktopGLCursor
    -      - DesktopGLPreferences

    Window
    ------

    -      - DesktopGLWindow
    -      - DesktopGLWindowConfiguration
    -      - DesktopGLWindowAdapter
    -      - IDesktopGLWindowListener

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

BACKENDS/DESKTOPGL/AUDIO
------------------------

    -      - GdxSoundAudioRecorder
    -      - IGLAudio
    -      - Mp3
    -      - Ogg
    -      - OggInputStream
    -      - OpenALAudio
    -      - OpenALAudioDevice
    -      - OpenALMusic
    -      - OpenALSound
    -      - Wav

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

BACKENDS/DESKTOPGL/AUDIO/MOCK
-----------------------------

    -      - MockAudio
    -      - MockAudioDevice
    -      - MockAudioRecorder
    -      - MockMusic
    -      - MockSound

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

EXTENSIONS/BOX2D
----------------

    - It's most likely best to recommend the use of an already available Python port.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

EXTENSIONS/GDX-TOOLS
--------------------

    -      - FileProcessor

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

EXTENSIONS/GDX-TOOLS/TILEDMAPPACKER
-----------------------------------

    -      - TileMapPacker
    -      - TiledMapPackerTest
    -      - TiledMapPackerTestRender
    -      - TileSetLayout

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

EXTENSIONS/GDX-TOOLS/TOOLS
--------------------------

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

EXTENSIONS/GDX-TOOLS/TOOLS/TEXTUREPACKER
----------------------------------------

    -      - ColorBleedEffect
    -      - TexturePacker

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

EXTENSIONS/GDX-TOOLS/IMAGEPACKER
--------------------------------

    -      - ImagePacker

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

