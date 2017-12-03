import io
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
  def visualize_labeled_images(images, labels, max_outputs=3, name='image'):    
  def _visualize_image(image, label):   
     
        # Do the actual drawing in python
        fig = plt.figure(figsize=(3, 3), dpi=80)
        ax = fig.add_subplot(111)
        ax.imshow(image[::-1,...])
        ax.text(0, 0, str(label), 
          horizontalalignment='left', 
          verticalalignment='top')
        fig.canvas.draw()        

        # Write the plot as a memory file.
        buf = io.BytesIO()
        data = fig.savefig(buf, format='png')
        buf.seek(0)   
             # Read the image and convert to numpy array
        img = PIL.Image.open(buf)        
        return np.array(img.getdata()).reshape(img.size[0], img.size[1], -1)    
   def _visualize_images(images, labels):   
             
        # Only display the given number of examples in the batch
        outputs = []        
        for i in range(max_outputs):
            output = _visualize_image(images[i], labels[i])
            outputs.append(output)        
        return np.array(outputs, dtype=np.uint8)    
        
   # Run the python op.
   figs = tf.py_func(_visualize_images, [images, labels], tf.uint8)    
   return tf.summary.image(name, figs)