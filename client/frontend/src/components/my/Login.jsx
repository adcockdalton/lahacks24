import React, { useEffect } from "react";
import styled from "styled-components";

import { ChevronsLeft, ChevronsRight } from "lucide-react";

import { format } from "date-fns";
import { Calendar as CalendarIcon } from "lucide-react";

import { cn } from "./../../lib/utils";
import { Popover, PopoverContent, PopoverTrigger } from "./../ui/popover";
import { Button } from "./../ui/button";

import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "./../ui/card";

import { Calendar } from "./../ui/calendar";

const Title = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 5rem;
`;

function Login() {
    const [date, setDate] = React.useState(new Date("January 1, 2000"));

    useEffect(() => {
        // TODO
    }, [date]);

    return (
        <div className="flex flex-col justify-evenly h-screen">
            <Title>title (no styling yet)</Title>
            <div className="flex items-center justify-center">
                <Card className="w-[350px]">
                    <CardHeader>
                        <CardTitle>Login</CardTitle>
                        <CardDescription className="py-3">
                            Let's get to know you <span>😊</span>
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        <Popover>
                            <PopoverTrigger asChild>
                                <Button
                                    variant={"outline"}
                                    className={cn(
                                        "w-[280px] justify-start text-left font-normal",
                                        !date && "text-muted-foreground"
                                    )}
                                >
                                    <CalendarIcon className="mr-2 h-4 w-4" />
                                    {date ? (
                                        format(date, "PPP")
                                    ) : (
                                        <span>Pick a date</span>
                                    )}
                                </Button>
                            </PopoverTrigger>
                            <PopoverContent className="flex w-auto flex-col justify-center pt-6">
                                <Calendar
                                    mode="single"
                                    selected={date}
                                    onSelect={setDate}
                                    defaultMonth={date}
                                />
                                <div className="flex justify-around">
                                    <Button
                                        className="h-7 w-7 p-0 bg-slate-900 opacity-100 hover:opacity-80"
                                        onClick={() =>
                                            setDate(
                                                new Date(
                                                    date.setFullYear(
                                                        date.getFullYear() - 1
                                                    )
                                                )
                                            )
                                        }
                                    >
                                        <ChevronsLeft className="h-4 w-4"></ChevronsLeft>
                                    </Button>
                                    <div className="flex flex-col justify-center">
                                        <p className="text-sm font-medium">
                                            Pick your birthday!
                                        </p>
                                    </div>
                                    <Button
                                        className="h-7 w-7 p-0 bg-slate-900 opacity-100 hover:opacity-80"
                                        onClick={() =>
                                            setDate(
                                                new Date(
                                                    date.setFullYear(
                                                        date.getFullYear() + 1
                                                    )
                                                )
                                            )
                                        }
                                    >
                                        <ChevronsRight className="h-4 w-4"></ChevronsRight>
                                    </Button>
                                </div>
                            </PopoverContent>
                        </Popover>
                    </CardContent>
                    <CardFooter>
                        <Button>Go!</Button>
                    </CardFooter>
                </Card>
            </div>
        </div>
    );
}

export default Login;
