[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SdXSjEmH)
# EV-HW3: PhysGaussian

This homework is based on the recent CVPR 2024 paper [PhysGaussian](https://github.com/XPandora/PhysGaussian/tree/main), which introduces a novel framework that integrates physical constraints into 3D Gaussian representations for modeling generative dynamics.

You are **not required** to implement training from scratch. Instead, your task is to set up the environment as specified in the official repository and run the simulation scripts to observe and analyze the results.


## Getting the Code from the Official PhysGaussian GitHub Repository
Download the official codebase using the following command:
```
git clone https://github.com/XPandora/PhysGaussian.git
```


## Environment Setup
Navigate to the "PhysGaussian" directory and follow the instructions under the "Python Environment" section in the official README to set up the environment.


## Running the Simulation
Follow the "Quick Start" section and execute the simulation scripts as instructed. Make sure to verify your outputs and understand the role of physics constraints in the generated dynamics.


## Homework Instructions
Please complete Part 1–2 as described in the [Google Slides](https://docs.google.com/presentation/d/13JcQC12pI8Wb9ZuaVV400HVZr9eUeZvf7gB7Le8FRV4/edit?usp=sharing).


# Reference
```bibtex
@inproceedings{xie2024physgaussian,
    title     = {Physgaussian: Physics-integrated 3d gaussians for generative dynamics},
    author    = {Xie, Tianyi and Zong, Zeshun and Qiu, Yuxing and Li, Xuan and Feng, Yutao and Yang, Yin and Jiang, Chenfanfu},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    year      = {2024}
}
```

# Part 1

I choose jelly and snow for my simulation, which use `configs/jelly.json` and `configs/snow.json` as config respectivly.

[Youtube](https://youtu.be/FdosllQtX_E)

# Part 2

## n_grid

`n_grid`: 50 -> 25

configs:
- jelly: `configs/jelly_n_grid.json`
- snow: `configs/snow_n_grid.json`

| material | jelly | snow  |
|---------:|:-----:|:-----:|
|     psnr | 21.96 | 15.20 |

The motion becomes smaller when n_grid decreases, but the motion last the same amount of time.

## substeps

`substep_dt`: 1e-4 -> 5e-5

configs:
- jelly: `configs/jelly_substep_dt.json`
- snow: `configs/snow_substep_dt.json`

| material | jelly | snow  |
|---------:|:-----:|:-----:|
|     psnr | 22.08 | 14.87 |

Similar to `n_grid` the motion becomes smaller when substeps increases (`substep_dt` decreases), but the motion last the same amount of time.

## grid_v_damping_scale

`grid_v_damping_scale`: 0.9999 -> 0.999

configs:
- jelly: `configs/jelly_grid_v_damping_scale_down.json`
- snow: `configs/snow_grid_v_damping_scale_down.json`

| material | jelly | snow  |
|---------:|:-----:|:-----:|
|     psnr | 21.71 | 14.65 |

When the damping scale decreses, the motion stops faster since it is damped more.

## softening

`softening`: 0.1 -> 0.01

configs:
- jelly: `configs/jelly_softening.json`
- snow: `configs/snow_softening.json`
- plasticine: `configs/plasticine_softening.json`

| material | jelly | snow  | plasticine |
|---------:|:-----:|:-----:|:----------:|
|     psnr | 76.23 | 37.28 |    76.18   |

Changing `softening` doesn't effect the result, overall the rendered motion are the same. Even the after trace code that `softening` is only used in `plasticine` material, it also doesn't effect `plasticine` reuslts.

# BONUS

I would make the material-related parameters as trainable parameters and record real world video as training data to finetune the exsisting model.