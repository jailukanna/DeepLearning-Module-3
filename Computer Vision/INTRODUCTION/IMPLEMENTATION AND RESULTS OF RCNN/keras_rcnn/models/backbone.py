# -*- coding: utf-8 -*-

import keras_resnet.models
import tensorflow


def ResNet50():
    def f(x):
        y = keras_resnet.models.ResNet50(include_top=False, inputs=x)

        _, _, convolution_4, _ = y.outputs

        return convolution_4

    return f


def VGG16():
    def f(x):
        y = tensorflow.keras.applications.VGG16(include_top=False, input_tensor=x)

        return y.layers[-3].output

    return f


def VGG19():
    def f(x):
        y = tensorflow.keras.applications.VGG19(include_top=False, input_tensor=x)

        return y.layers[-3].output

    return f
