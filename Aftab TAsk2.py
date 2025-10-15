{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62500412-d97d-4de8-84e5-d1b97edc8844",
   "metadata": {},
   "outputs": [],
   "source": [
    "# roll no = 042\n",
    "#aftab ali "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1efe1407-b71e-4e97-abf4-f3d4d509150a",
   "metadata": {},
   "outputs": [],
   "source": [
    "films = [\n",
    "    (\"Eternal Sunshine of the Spotless Mind\", 20000000),\n",
    "    (\"Memento\", 9000000),\n",
    "    (\"Requiem for a Dream\", 4500000),\n",
    "    (\"Pirates of the Caribbean: On Stranger Tides\", 379000000),\n",
    "    (\"Avengers: Age of Ultron\", 365000000),\n",
    "    (\"Avengers: Endgame\", 356000000),\n",
    "    (\"Incredibles 2\", 200000000)\n",
    "]\n",
    "\n",
    "more = input(\"Would you like to add more films? (yes/no) \").strip().lower()\n",
    "\n",
    "if more == \"yes\":\n",
    "    num = int(input(\"How many films do you want to add? \"))\n",
    "    for _ in range(num):\n",
    "        title = input(\"Enter film title: \")\n",
    "        cost = int(input(\"Enter film budget: \"))\n",
    "        films.append((title, cost))\n",
    "\n",
    "sum_budget = sum(amount for _, amount in films)\n",
    "avg_budget = sum_budget / len(films)\n",
    "\n",
    "print(f\"\\nAverage film budget: ${avg_budget:.2f}\")\n",
    "\n",
    "over_avg = []\n",
    "for title, cost in films:\n",
    "    if cost > avg_budget:\n",
    "        gap = cost - avg_budget\n",
    "        over_avg.append((title, gap))\n",
    "        print(f\"\\n{title} is above average by ${gap:.2f}\")\n",
    "\n",
    "print(f\"\\nTotal films above average: {len(over_avg)}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5ee9931-a2ab-49c3-a41a-6169f698b423",
   "metadata": {},
   "outputs": [],
   "source": [
    "for num in range(1, 101):\n",
    "    if num % 3 == 0 and num % 5 == 0:\n",
    "        print(\"FizzBuzz\")\n",
    "    elif num % 3 == 0:\n",
    "        print(\"Fizz\")\n",
    "    elif num % 5 == 0:\n",
    "        print(\"Buzz\")\n",
    "    else:\n",
    "        print(num)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
