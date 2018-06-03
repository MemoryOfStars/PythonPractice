#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:27:14 2018

@author: kmkgmx
"""

import tensorflow as tf
import numpy as np

trX = np.linspace(-1,1,101)
trY = 2*trX + np.random.randn(*trX.shape) * 0.33

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

def model(X,W):
    return tf.multiply(X,W)


W = tf.Variable(0.0,"Weight")
B = tf.Variable(0.0,"Bias")
y_model = model(X,W) + B

cost = tf.square(Y - y_model)

train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    
    for i in range(100):
        for (x,y) in zip(trX,trY):
            sess.run(train_op,feed_dict={X:x,Y:y})
    
    print(sess.run(W))
    print(sess.run(B))



