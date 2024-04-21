import React, { useEffect, useState } from 'react';
import { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent } from './CardComponents';

const EventCard = ({ response }) => {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/getRelatedEvent', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => setData(data))
        .catch(error => console.error(error));
    }, []);

    if (!data) {
        return <div>Loading...</div>;
    }

    return (
        <Card className="m-4">
            <CardHeader>
                <CardTitle>{data.title}</CardTitle>
            </CardHeader>
            <CardContent>
                <CardDescription>{data.description}</CardDescription>
            </CardContent>
            <CardFooter>
                {data.county}
            </CardFooter>
        </Card>
    );
};

export default EventCard;