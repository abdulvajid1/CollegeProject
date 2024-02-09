from cx_Freeze import setup,Executable


setup(
    name = 'Ai Gesture Controlled virtual mouse',
    version='1.0',
    author='None',
    description='virtual mouse',
    executables=[
    Executable('src\Gesture_Controller.py',
    shortcut_name='Ai mouse'       
               )]

)