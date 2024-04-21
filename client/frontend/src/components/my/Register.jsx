import React from "react";
import { useEffect } from "react";
import styled from "styled-components";

import { ChevronsRight } from "lucide-react";

import { useNavigate, useParams } from "react-router-dom";

import { Calendar as CalendarIcon, UserRound as User } from "lucide-react";

import { Button } from "./../ui/button";

import { Input } from "./../ui/input";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";


import {
    Form,
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "./../ui/form";

import {
    Card,
    CardContent,
    CardTitle,
    CardDescription,
    CardFooter,
    CardHeader,
} from "./../ui/card";

import BackgroundGraphic from "./../../assets/bg2.svg";

const Title = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 10rem;
    font-family: "Dela Gothic One", cursive;
`;

const Background = styled.div`
    background-image: url(${BackgroundGraphic});
    background-color: #ffffff;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center bottom;
    height: 100vh;
    flex: 1;
    flex-direction: column;
    justify-content: space-evenly;
`;

const FormSchema = z.object({
    answer: z.string().min(10, {
        message: "Answer must be at least 10+ characters.",
    }),
});

function Register() {
    const navigate = useNavigate();
    const {UUID} = useParams();
    console.log(UUID);
    const [question, setQuestion] = React.useState("");

    const form = useForm({
        resolver: zodResolver(FormSchema),
        defaultValues: {
            answer: "",
        },
    });

    useEffect(() => {
        fetch('http://127.0.0.1:8000/question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ uuid: UUID })
        })
            .then(response => response.json())
            .then(data => setQuestion(data.question));  // Replace 'question' with the actual key in the response
        form.reset();
    }, [UUID]);

    async function onSubmit(data) {
        console.log(data);
        //Add UUId to data
        data["uuid"] = UUID;
        const response = await fetch('http://127.0.0.1:8000/setAnswer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
    
        if (response.ok) {
            //fetch 'http://127.0.0.1:8000/question' for the next question
            fetch('http://127.0.0.1:8000/question', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ uuid: UUID })
            })
                .then(response => response.json())
                .then(data => setQuestion(data.question));
            form.reset();
        } else {
            // Handle error
            console.error('Failed to login:', response);
        }
    }

    return (
        <Background>
            <Title>TagAlong</Title>
            <div className="flex items-center justify-center">
                <Card className="w-[280px]">
                    <CardHeader>
                        <CardTitle>
                        Let's know you better! {":)"}
                        </CardTitle>
                        <CardDescription className="flex justify-center">
                            {question}
                        </CardDescription>
                    </CardHeader>
                    <CardContent className="flex items-center">
                        <Form {...form}>
                            <form
                                onSubmit={form.handleSubmit(onSubmit)}
                                className="space-y-6 w-full"
                            >
                                <FormField
                                    control={form.control}
                                    name="answer"
                                    render={({ field }) => (
                                        <FormItem>
                                            <FormLabel>Answer</FormLabel>
                                            <div className="flex items-center">
                                                <User className="mr-3 h-4 w-4" />
                                                <FormControl>
                                                    <Input
                                                        {...field}
                                                        placeholder={
                                                            ""
                                                        }
                                                    />
                                                </FormControl>
                                            </div>
                                            <FormMessage></FormMessage>
                                        </FormItem>
                                    )}
                                />

                                <Button
                                    className="w-1/4 bg-peach "
                                    type="submit"
                                >
                                    <ChevronsRight className="size-4" />
                                </Button>
                            </form>
                        </Form>
                    </CardContent>
                </Card>
            </div>
        </Background>
    );
}

export default Register;
