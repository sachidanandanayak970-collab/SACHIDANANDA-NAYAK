{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMpKf6LpLnveVvlnwPFli+B",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sachidanandanayak970-collab/SACHIDANANDA-NAYAK/blob/main/Python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_CGTDynrSImX",
        "outputId": "6741f8b9-777c-4a66-ee35-78ad911fcb63"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 4\n",
            "The number is Even\n"
          ]
        }
      ],
      "source": [
        "num = int(input(\"Enter a number: \"))\n",
        "\n",
        "if num % 2 == 0:\n",
        "    print(\"The number is Even\")\n",
        "else:\n",
        "    print(\"The number is Odd\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1, 11):\n",
        "    print(i, end=\" \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D4jlJxg-Ssh2",
        "outputId": "b9beff45-dbf7-4a5e-ebde-632834ab2626"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5 6 7 8 9 10 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# create a list of 5 numbers\n",
        "numbers = [1, 2, 3, 4, 5]\n",
        "\n",
        "# print square of each number\n",
        "for num in numbers:\n",
        "    print(\"Square of\", num, \"is\", num ** 2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "97KPlp9QTDzc",
        "outputId": "530ff152-ef11-4091-baa4-93206cd5509d"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Square of 1 is 1\n",
            "Square of 2 is 4\n",
            "Square of 3 is 9\n",
            "Square of 4 is 16\n",
            "Square of 5 is 25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# create a list of 5 numbers\n",
        "numbers = [5, 2, 9, 1, 7]\n",
        "\n",
        "# add a new number\n",
        "numbers.append(4)\n",
        "\n",
        "# sort the list\n",
        "numbers.sort()\n",
        "\n",
        "# print the final list\n",
        "print(\"Sorted list:\", numbers)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1Owof-YDTbXK",
        "outputId": "f144fc12-7d94-4d72-9718-0828532c81bf"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sorted list: [1, 2, 4, 5, 7, 9]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# create a list\n",
        "numbers = [5, 2, 9, 1, 7]\n",
        "\n",
        "# find the largest number\n",
        "largest = max(numbers)\n",
        "\n",
        "# remove the largest number\n",
        "numbers.remove(largest)\n",
        "\n",
        "# print the updated list\n",
        "print(\"List after removing largest number:\", numbers)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_jWL5OYJUDAP",
        "outputId": "56e28585-6dc0-49d2-82f3-b173d00a2806"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "List after removing largest number: [5, 2, 1, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# create a dictionary\n",
        "students = {\n",
        "    \"HAPPY\": 85,\n",
        "    \"BISWAJIT\": 90,\n",
        "    \"UMAKANTA\": 78,\n",
        "    \"ARYAN\": 88,\n",
        "    \"SAI\": 92\n",
        "}\n",
        "\n",
        "# print the dictionary\n",
        "print(\"Student Marks:\")\n",
        "for name, marks in students.items():\n",
        "    print(name, \":\", marks)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BGDnwUBpUanZ",
        "outputId": "da9a0739-6f50-4d12-bb81-dad3619c3897"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Student Marks:\n",
            "HAPPY : 85\n",
            "BISWAJIT : 90\n",
            "UMAKANTA : 78\n",
            "ARYAN : 88\n",
            "SAI : 92\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# existing dictionary\n",
        "students = {\n",
        "    \"HAPPY\": 85,\n",
        "    \"BISWAJIT\": 90,\n",
        "    \"UMAKANTA\": 78\n",
        "}\n",
        "\n",
        "# add a new student\n",
        "students[\"ARYAN\"] = 88\n",
        "\n",
        "# update marks of an existing student\n",
        "students[\"SATYA\"] = 95\n",
        "\n",
        "# print updated dictionary\n",
        "print(\"Updated Student Marks:\")\n",
        "for name, marks in students.items():\n",
        "    print(name, \":\", marks)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YUpyNRR9Vhqw",
        "outputId": "af310697-3bc2-4fa1-be44-decbcb1c8c5d"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Updated Student Marks:\n",
            "HAPPY : 85\n",
            "BISWAJIT : 90\n",
            "UMAKANTA : 78\n",
            "ARYAN : 88\n",
            "SATYA : 95\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "total = 0\n",
        "num = 1\n",
        "\n",
        "while total <= 100:\n",
        "    total += num\n",
        "    num += 1\n",
        "\n",
        "print(\"Final sum:\", total)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mrX9wkfSVwY5",
        "outputId": "83775a0e-d278-485e-c209-2fee2f282347"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Final sum: 105\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# take two numbers as input\n",
        "num1 = float(input(\"Enter first number: \"))\n",
        "num2 = float(input(\"Enter second number: \"))\n",
        "\n",
        "# perform arithmetic operations\n",
        "addition = num1 + num2\n",
        "subtraction = num1 - num2\n",
        "multiplication = num1 * num2\n",
        "\n",
        "# check for division by zero\n",
        "if num2 != 0:\n",
        "    division = num1 / num2\n",
        "else:\n",
        "    division = \"Undefined (cannot divide by zero)\"\n",
        "\n",
        "# display results\n",
        "print(\"Addition:\", addition)\n",
        "print(\"Subtraction:\", subtraction)\n",
        "print(\"Multiplication:\", multiplication)\n",
        "print(\"Division:\", division)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Tc2nQt5bWbvd",
        "outputId": "e17a8893-9153-4891-e18b-82fe180014dd"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 5\n",
            "Enter second number: 4\n",
            "Addition: 9.0\n",
            "Subtraction: 1.0\n",
            "Multiplication: 20.0\n",
            "Division: 1.25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def factorial(n):\n",
        "    \"\"\"Function to return factorial of a number\"\"\"\n",
        "    if n == 0 or n == 1:\n",
        "        return 1\n",
        "    else:\n",
        "        result = 1\n",
        "        for i in range(2, n + 1):\n",
        "            result *= i\n",
        "        return result\n",
        "\n",
        "# example usage\n",
        "num = int(input(\"Enter a number: \"))\n",
        "print(f\"Factorial of {num} is {factorial(num)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y_W1P8uRWzWN",
        "outputId": "011335be-4c14-4aed-ea38-d52dce33da96"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 5\n",
            "Factorial of 5 is 120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def is_palindrome(s):\n",
        "    \"\"\"Function to check if a string is a palindrome\"\"\"\n",
        "    # remove spaces and convert to lowercase for uniformity\n",
        "    s = s.replace(\" \", \"\").lower()\n",
        "    # check if string is same forwards and backwards\n",
        "    return s == s[::-1]\n",
        "\n",
        "# example usage\n",
        "string = input(\"Enter a string: \")\n",
        "if is_palindrome(string):\n",
        "    print(f'\"{string}\" is a palindrome')\n",
        "else:\n",
        "    print(f'\"{string}\" is not a palindrome')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EsyBaHxGW3DS",
        "outputId": "bc4173c5-b595-45da-fde9-7bdfaaa8a2bc"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a string: 5\n",
            "\"5\" is a palindrome\n"
          ]
        }
      ]
    }
  ]
}