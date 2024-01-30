#include <Python.h>

/**
* print_python_string - Print information
* about a Python string object
* @p: Pointer to a Python object
*/
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p)
			? "compact ascii" : "compact unicode object");
		Py_ssize_t length = PyUnicode_GET_LENGTH(p);
		Py_UNICODE *value = PyUnicode_AS_UNICODE(p);

		printf("  length: %ld\n", length);
		printf("  value: %ls\n", value);
	}
	else
	{
		fprintf(stderr, "[.] string object info\n");
		fprintf(stderr, "  [ERROR] Invalid String Object\n");
	}
}

/**
* main - Entry point of the program
*
* This program demonstrates the usage of the print_python_string function.
* It prints information about Python string objects.
*
* Return: Always returns 0 to indicate successful execution.
*/
int main(void)
{
	PyObject *s = PyUnicode_DecodeUTF8("The spoon does not exist", 24, NULL);

	print_python_string(s);
	Py_DECREF(s);

	s = PyUnicode_DecodeUTF8("ложка не существует", 19, NULL);
	print_python_string(s);
	Py_DECREF(s);

	s = PyUnicode_DecodeUTF8("La cuillère n'existe pas", 24, NULL);
	print_python_string(s);
	Py_DECREF(s);

	s = PyUnicode_DecodeUTF8("勺子不存在", 5, NULL);
	print_python_string(s);
	Py_DECREF(s);

	s = PyUnicode_DecodeUTF8("숟가락은 존재하지 않는다.", 14, NULL);
	print_python_string(s);
	Py_DECREF(s);

	s = PyUnicode_DecodeUTF8("スプーンは存在しない", 10, NULL);
	print_python_string(s);
	Py_DECREF(s);

	PyObject *b = PyBytes_FromString("The spoon does not exist");

	print_python_string(b);
	Py_DECREF(b);

	return (0);
}

