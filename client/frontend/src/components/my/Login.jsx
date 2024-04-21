import React from "react";
import styled from "styled-components";

import { ChevronsRight } from "lucide-react";

import { useNavigate } from "react-router-dom";

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
    name: z.string().min(4, {
        message: "Name must be 4+ characters.",
    }),
    birthday: z.coerce.date(),
});

function Login() {
    const navigate = useNavigate();

    const form = useForm({
        resolver: zodResolver(FormSchema),
        defaultValues: {
            name: "",
            birthday: "",
        },
    });

    function onSubmit(data) {
        console.log(data);
        navigate("/register");
    }

    return (
        <Background>
            <Title>TagAlong</Title>
            <div className="flex items-center justify-center">
                <Card className="w-[280px]">
                    <CardHeader>
                        <CardDescription className="flex justify-center">
                            Let's get to know you {":)"}
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
                                    name="name"
                                    render={({ field }) => (
                                        <FormItem>
                                            <FormLabel>Name</FormLabel>
                                            <div className="flex items-center">
                                                <User className="mr-3 h-4 w-4" />
                                                <FormControl>
                                                    <Input
                                                        {...field}
                                                        placeholder={
                                                            "First Last"
                                                        }
                                                    />
                                                </FormControl>
                                            </div>
                                            <FormMessage></FormMessage>
                                        </FormItem>
                                    )}
                                />

                                <FormField
                                    control={form.control}
                                    name="birthday"
                                    render={({ field }) => (
                                        <FormItem>
                                            <FormLabel>Birthday</FormLabel>
                                            <div className="flex items-center">
                                                <CalendarIcon className="mr-3 h-4 w-4" />
                                                <FormControl>
                                                    <Input
                                                        {...field}
                                                        placeholder={
                                                            "YYYY-MM-DD"
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

export default Login;
