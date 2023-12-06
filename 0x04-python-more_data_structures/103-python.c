#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>

void print_python_list(PyObject *p)
{
    long int size;
    int x;
    const char *type;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

    for (x = 0; x < size; x++)
    {
        type = ((PyListObject *)p)->ob_item[x]->ob_type->tp_name;
        printf("Element %x: %s\n", x, type);
        if (!strcmp(type, "bytes"))
            print_python_bytes(((PyListObject *)p)->ob_item[x]);
    }
}

void print_python_bytes(PyObject *p)
{
    long int size;
    int x;
    char *str = NULL;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &str, &size);

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %li bytes:", size < 10 ? size : 10);
    
    for (x = 0; x < size && x < 10; x++)
        printf(" %02hhx", str[x]);
    
    printf("\n");
}
