import React from 'react';
import { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent } from './CardComponents';

const EventCard = ({ key, title, description, county }) => {
    return (
        <Card className="m-4">
            <CardHeader>
                <CardTitle>{title}</CardTitle>
            </CardHeader>
            <CardContent>
                <CardDescription>{description}</CardDescription>
            </CardContent>
            <CardFooter>
                {county}
            </CardFooter>
        </Card>
    );
};

export default EventCard;