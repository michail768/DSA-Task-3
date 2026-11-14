#define MAX 100
struct Deque
{
    int arr[MAX];
    int front, rear;
};

void initDeque(struct Deque *dq)
{
    dq->front = -1;
    dq->rear = -1;
}

// 1. Front Insertion
void insertFront(struct Deque *dq, int key)
{
    if ((dq->front == 0 && dq->rear == MAX - 1) || (dq->front == dq->rear + 1))
    {
        printf("Overflow\n");
        return;
    }
    if (dq->front == -1)
    {
        dq->front = 0;
        dq->rear = 0;
    }
    else if (dq->front == 0)
    {
        dq->front = MAX - 1;
    }
    else
    {
        dq->front = dq->front - 1;
    }
    dq->arr[dq->front] = key;
}

// 2. Rear Insertion
void insertRear(struct Deque *dq, int key)
{
    if ((dq->front == 0 && dq->rear == MAX - 1) || (dq->front == dq->rear + 1))
    {
        printf("Overflow\n");
        return;
    }
    if (dq->front == -1)
    {
        dq->front = 0;
        dq->rear = 0;
    }
    else if (dq->rear == MAX - 1)
    {
        dq->rear = 0;
    }
    else
    {
        dq->rear = dq->rear + 1;
    }
    dq->arr[dq->rear] = key;
}

// 3. Front Deletion
void deleteFront(struct Deque *dq)
{
    if (dq->front == -1)
    {
        printf("Underflow\n");
        return;
    }
    if (dq->front == dq->rear)
    {
        dq->front = -1;
        dq->rear = -1;
    }
    else if (dq->front == MAX - 1)
    {
        dq->front = 0;
    }
    else
    {
        dq->front = dq->front + 1;
    }
}

// 4. Rear Deletion
void deleteRear(struct Deque *dq)
{
    if (dq->front == -1)
    {
        printf("Underflow\n");
        return;
    }
    if (dq->front == dq->rear)
    {
        dq->front = -1;
        dq->rear = -1;
    }
    else if (dq->rear == 0)
    {
        dq->rear = MAX - 1;
    }
    else
    {
        dq->rear = dq->rear - 1;
    }
}