!README.txt
By: Sam Schmitz

This 3d Renderer was made during my CS260 class (computer graphics). It uses 3d rendering to create different scenes and animations. The renderer is able to render 3d models (basic shapes and meshes), use multiple light sources and move the camera. 3d models can be translated and transformed using matricies and scenes can be pieced together to form animations. Below you will find a record of the different versions of the renderer. For our final project me and my partner, Zach Abbey, created an animation which is located as final.gif. 

Different Versions:

Version 3:
    Description: updates the lighting/shading for more realism
    Things Added: Blinn-phong style rendering, Repositional light sources, Multiple light sources, Shadows
  Version 4:
    Description:  Adds mappable textures to objects
    Things Added: Box and Sphere textures
  Version 5:
    Description: Adds translations (of objects and the camera) to the scene.
    Things Added: trans3d (allows translation of 3d objects to locations in the scene), Movable Camera, Transformable class (manipulation of 3d objects)
  Version 6:
    Description: Adds a mesh that can render/model any object no matter the shape.
    Things Added: Triangle Class, Basic Meshes
  Version 7:
    Description: Adds animation, run_prt (multiprocessing for rendering), Cylinder class, and complex meshes
    Things Added: animation, multiprocessing, Cylinder class, and complex meshes
    Made in collaberation with Zach Abbey

Final Project:
  Description:
    Made an animation of a desk that has things moving on it
  Things added:
    animation
    made run_prt work - uses multiprocessing for rendering
    Cylinder class: The normals and end sides(circles) didn't work right
                    so we didn't end up using this in the project
    Complex Meshes: Several complex meshes were used(The Batmobile)
  
  Scene Location: /final.gif
