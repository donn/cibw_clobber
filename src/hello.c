#include <Python.h>

static PyObject *
helloworld(PyObject *self, PyObject *args)
{
    printf("Hello, world!\n");

    Py_RETURN_NONE;
}

static PyMethodDef methods[] = {
    {"helloworld", helloworld, METH_VARARGS, "Print Hello, World!"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduleDef = {
    PyModuleDef_HEAD_INIT,
    "_helloworld",
    "",
    -1,
    methods
};

PyMODINIT_FUNC
PyInit__helloworld(void)
{
    return PyModule_Create(&moduleDef);
}
