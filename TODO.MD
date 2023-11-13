- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LIBGDX CPP CONVERSION - ROUND 1
----------------------------------

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- STEP 1: Complete all conversions so that the code will build.
- STEP 2: Refactor, where possible and necessary, to take advantage of C++ language features.
- STEP 3: Resolve ALL remaining TODOs.
- STEP 4: Ensure code is fully documented.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- NO MAGIC NUMBERS!!!
- 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- SORT OUT VERSIONING!!!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- IP   = Conversion In Progress.
- DONE = Class finished

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- PRIORITY is 2D classes first

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- Restructure, where necessary, to cut the number of exceptions that can be thrown
- Constantly look for opportunities to improve this code.
- 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

ASSETS
------

    -      - AssetDescriptor                
    -      - AssetLoaderParameters          
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
    -      - I18NBundleLoader               
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
    -      - IFileHandleResolver
    -      - InternalFileHandleResolver
    -------------------------------------
    -      - ClasspathFileHandleResolver   
    -      - ExternalFileHandleResolver    
    -      - LocalFileHandleResolver       
    -      - PrefixFileHandleResolver      
    -      - ResolutionFileResolver        
    -------------------------------------

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
    - DONE - IGraphics                      
    - DONE - IInput                         
    - DONE - IInputProcessor                
    - DONE - ILifecycleListener             
    -      - INet                           
    - DONE - InputAdapter                   
    -      - InputEventQueue      
    - DONE - InputMultiplexor
    - DONE - IPreferences                   
    - DONE - IScreen                        
    - DONE - ScreenAdapter                  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FILES
-----

    - java.io.BufferedReader                -> 
    - java.io.BufferedInputStream           -> 
    - java.io.ByteArrayOutputStream         -> 
    - java.io.DataInputStream               -> 
    - java.io.DataOutputStream              -> 
    - java.io.File                          -> 
    - java.io.FileHandle                    -> 
    - java.io.FileInputStream               -> 
    - java.io.FileOutputStream              -> 
    - java.io.DataOuput                     -> 
    - java.io.InputStream                   -> 
    - java.io.InputStreamReader             -> 
    - java.io.IOException                   -> 
    - java.io.OutputStream                  -> 
    - java.io.Reader                        -> 

    - Would MemoryStream cover all these?

    - java.nio.Buffer                       ->  
    - java.nio.BufferUtils                  ->  
    - java.nio.ByteBuffer                   ->  
    - java.nio.ByteBuffer                   -> 
    - java.nio.CharBuffer                   -> 
    - java.nio.DataBuffer                   -> 
    - java.nio.DirectByteBuffer             -> 
    - java.nio.DoubleBuffer                 -> 
    - java.nio.FloatBuffer                  -> 
    - java.nio.HeapLongBuffer               -> 
    - java.nio.IntBuffer                    -> 
    - java.nio.LongBuffer                   -> 

    ------------------------------------------

    - java.util.zip.CRC32                   -> 
    - java.util.zip.CheckedOutputStream     -> 
    - java.util.zip.Deflater                -> 
    - java.util.zip.DeflaterOutputStream    -> 
    - java.util.zip.InflaterInputStream     -> 

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

GRAPHICS/GLUTILS
----------------

    -      - ETC1                                   Should I support this format?
    -      - ETC1TextureData                        Should I support this format?
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

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

GRAPHICS/PROFILING
------------------

    -      - GL20Interceptor
    -      - GL30Interceptor
    -      - GL31Interceptor
    -      - GL32Interceptor
    -      - GLInterceptor
    -      - GLProfiler
    -      - IGLErrorListener

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

INPUT
-----

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

    -      - TideMapLoader

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

MATH
----

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

NETWORK
-------

    -      - HttpParametersUtils
    -      - HttpRequestBuilder
    -      - HttpStatus
    -      - IHttpRequestHeader
    -      - IHttpResponseHeader
    -      - IServerSocket
    -      - ISocket
    -      - NetJavaImpl
    -      - NetJavaServerSocketImpl
    -      - NetJavaSocketImpl
    -      - ServerSocketHints
    -      - SocketHints

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

SCENES/LISTENERS
----------------

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

SCENES/SCENE2D
--------------

    -      - Action                         
    -      - Actor                          
    -      - Event                          
    -      - Group                          
    -      - InputEvent                     
    -      - Stage                          
    -      - Touchable                      
    -      - TouchFocus                     

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

SCENES.SCENE2D/ACTIONS
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

SCENES.SCENE2D/UI
-----------------

    -      - Button                         
    -      - ButtonGroup                    
    -      - Cell                           
    -      - CheckBox                       
    -      - Container                      
    -      - Dialog                         
    -      - HorizontalGroup                
    -      - Image                          
    -      - ImageButton                    
    -      - ImageTextButton                
    -      - Label                          
    -      - List                           
    -      - ParticleEffectActor            
    -      - ProgressBar                    
    -      - ScrollPane                     
    -      - SelectBox                      
    -      - Skin                           
    -      - Slider                         
    -      - SplitPane                      
    -      - Stack                          
    -      - Table                          
    -      - TextArea                       
    -      - TextButton                     
    -      - TextField                      
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

SCENES.SCENE2D/UTILS
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
    -      - DataInput                      
    -      - DataOutput                     
    -      - DataUtils                      
    -      - FloatConsts                    
    -      - ICloseable                     
    -      - IClipboard                                     
    -      - IRunnable                      
    -      - Logger                         
    -      - PerformanceCounter             
    -      - PerformanceCounters            
    -      - PropertiesUtils                
    -      - QuadTreeFloat
    -      - QuickSelect
    -      - Scaling
    -      - ScreenUtils
    -      - Select                         
    -      - Sort
    -      - StringTokenizer
    -      - Timer                          
    -      - TimeUtils
    -      - TimSort
    -      - Trace                          

    -      - GdxNativesLoader               
    -      - LittleEndianInputStream        
    -      - PauseableThread                
    -      - SharedLibraryLoader            
    -      - StreamUtils                    

    -      - Base64Coder                    
    -      - I18NBundle                     
    -      - Queue                          
    -      - SortedIntList                  
    -      - StringBuilder                  
    -      - TextFormatter                  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/ASYNC
-----------

    -      - AsyncExecutor
    -      - 
    -      - 
    -      - 
    -      - 

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/BUFFERS
-------------

    -      - Buffer
    -      - BufferUtils
    -      - ByteBuffer
    -      - CharBuffer
    -      - FloatBuffer
    -      - StringCharBuffer
    -      - DirectByteBuffer
    -      - DoubleBuffer
    -      - HeapByteBuffer
    -      - HeapCharBuffer
    -      - IDirectBuffer
    -      - IntBuffer
    -      - LongBuffer
    -      - MappedByteBuffer
    -      - ShortBuffer

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/COLLECTIONS
-----------------

    -      - Array<T>                      
    -      - Collections
    -      - DelayedRemovalArray           
    -      - IdentityMap<K, V>             
    -      - ObjectMap                     
    -      - SnapshotArray<T>              

    -      - ArrayMap                      
    -      - ArrayIterable                 
    -      - ArrayIterator                 
    -      - BoolArray                     
    -      - ByteArray                     
    -      - CharArray                     
    -      - FloatArray                    
    -      - IntArray                      
    -      - IntFloatMap                   
    -      - IntIntMap                     
    -      - IntMap                        
    -      - IntSet                        
    -      - IPredicate
    -      - LongArray                     
    -      - LongMap                       
    -      - ObjectFloatMap                
    -      - ObjectIntMap                  
    -      - ObjectLongMap                 
    -      - ObjectSet<T>                  
    -      - OrderedMap<K, V>              
    -      - OrderedSet<T>                 
    -      - PredicateIterable
    -      - PredicateIterator
    -      - ShortArray                    

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

UTILS/EXCEPTIONS
----------------

    -      - AssetNotLoadedException        
    -      - BufferOverflowException        
    -      - BufferUnderflowException       
    -      - GdxRuntimeException            
    -      - IllegalStateException          
    -      - InvalidMarkException       
    -      - MemberNullException
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

    -      - XmlReader
    -      - XmlReaderData
    -      - XmlWriter

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
