# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:45:17 2017

@author: abhil
"""

import tensorflow as tf
hello = tf.constant('Hello Tensorflow!')
sess = tf.Session()
print(sess.run(hello))
