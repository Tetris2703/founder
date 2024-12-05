
## Создание сопрограммы


```python
import asyncio

async def my_coroutine():
    print('Hello, world!')

# Чтобы выполнить сопрограмму, нужно использовать asyncio.run
asyncio.run(my_coroutine())
```
## Использование await
```python
import asyncio

async def say_hello():
    print('Hello')
    await asyncio.sleep(1)  # Приостановка на 1 секунду
    print('World!')

asyncio.run(say_hello())
```
## Создание задач
```python
import asyncio

async def say_hello():
    print('Hello')
    await asyncio.sleep(1)
    print('World!')

async def main():
    # Создаем задачу
    task = asyncio.create_task(say_hello())
    # Ждем завершения задачи
    await task

asyncio.run(main())
```
## Конкурентное выполнение задач
```python
import asyncio

async def say_hello():
    print('Hello')
    await asyncio.sleep(1)
    print('World!')

async def main():
    # Создаем три задачи
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_hello())
    task3 = asyncio.create_task(say_hello())

    # Ждем завершения всех задач
    await task1
    await task2
    await task3

asyncio.run(main())
```
## Снятие задач и тайм-ауты
```python
import asyncio

async def long_task():
    print('Starting long task')
    await asyncio.sleep(5)
    print('Long task finished')

async def main():
    task = asyncio.create_task(long_task())

    try:
        await asyncio.wait_for(task, timeout=2)
    except asyncio.TimeoutError:
        print('Task took too long, cancelling it')
        task.cancel()

asyncio.run(main())
```
## Использование asyncio.shield
```python
import asyncio

async def long_task():
    print('Starting long task')
    await asyncio.sleep(5)
    print('Long task finished')

async def main():
    task = asyncio.create_task(long_task())

    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=2)
    except asyncio.TimeoutError:
        print('Task is taking too long, but we will let it finish')
        await task

asyncio.run(main())
```
