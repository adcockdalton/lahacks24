import React, { useState, useEffect } from "react";
import { initializeApp } from "firebase/app";
import {
    getDatabase,
    ref,
    onValue,
    update,
    push,
    child,
    get,
    set,
    onChildAdded,
    onChildChanged,
} from "firebase/database";
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "./../ui/card";
import {
    Carousel,
    CarouselContent,
    CarouselItem,
    CarouselNext,
    CarouselPrevious,
} from "./../ui/carousel";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "./../ui/button";
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
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "../ui/select";
import styled from "styled-components";

import { Textarea } from "./../ui/textarea";
import { ScrollArea } from "../ui/scroll-area";
import { useParams } from "react-router-dom";

import BackgroundGraphic from "./../../assets/bg2.svg";
import { sub } from "date-fns";
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
    message: z
        .string()
        .min(1, { message: "Please enter a message" })
        .max(100, { message: "Message is too long" }),
    chat: z.string(),
});

const firebaseConfig = {
    apiKey: process.env.FIREBASE_API_KEY,
    authDomain: "tagalong-d9d3a.firebaseapp.com",
    databaseURL: "https://tagalong-d9d3a-default-rtdb.firebaseio.com",
    projectId: "tagalong-d9d3a",
    storageBucket: "tagalong-d9d3a.appspot.com",
    messagingSenderId: "258907556707",
    appId: "1:258907556707:web:3e1e8d4fe60af489676156",
};

const app = initializeApp(firebaseConfig);
const database = getDatabase(app);
const subscribedChats = ["123", "456"];

export default function Home() {
    const form = useForm({
        resolver: zodResolver(FormSchema),
    });

    const { userUUID } = useParams();

    function onSubmit(data) {
        const chatListRef = ref(database, `chats/${data.chat}/messages`);
        const newMessageRef = push(chatListRef);
        set(newMessageRef, {
            user: userUUID,
            content: data.message,
            chat: data.chat,
        });
    }

    const [globalData, setGlobalData] = useState({ chats: {} });

    useEffect(() => {
        for (let i = 0; i < subscribedChats.length; i++) {
            globalData.chats[subscribedChats[i]] = {};
            globalData.chats[subscribedChats[i]].messages = [];
            console.log("Global Data Now", globalData);

            /*
            const chatRef = ref(
                database,
                `chats/${subscribedChats.at[i]}/messages`
            );

            onChildAdded(chatRef, (data) => {
                console.log("Data from listener", data.val());
                try {
                    setGlobalData(
                        globalData.chats[subscribedChats[i]].messages.push(
                            data.val()
                        )
                    );
                } catch (e) {
                    console.log(e);
                }
            });
            */
        }
    }, []);

    const chatRef = ref(database, "/chats");

    onChildChanged(chatRef, (data) => {
        console.log("Data from listener", JSON.stringify(data.val()));
        console.log("data.key", data.key);
        console.log("data.val()", data.val());
        try {
            if (subscribedChats.includes(data.key)) {
                console.log("data.key in subscribedChats", data.key);
                globalData.chats[data.key] = data.val();
                setGlobalData(globalData);
                console.log("Global data set...", globalData);
            }
        } catch (e) {
            console.log(e);
        }
    });

    return (
        <Background>
            <div className="flex justify-center w-screen h-4/5 py-10">
                <Carousel className="max-w-xs">
                    <CarouselContent>
                        {subscribedChats.map((chat) => (
                            <CarouselItem key={chat} className="flex flex-col">
                                <div className="p-1">
                                    <Card>
                                        <CardHeader>
                                            <CardTitle>Chat #{chat}</CardTitle>
                                        </CardHeader>
                                        <CardContent className="flex flex-col w-full aspect-square justify-start px-6 py-2">
                                            <ScrollArea className="h-5/6 flex flex-col align-bottom">
                                                {globalData.chats[chat] &&
                                                globalData.chats[chat]
                                                    .messages &&
                                                Object.entries(
                                                    globalData.chats[chat]
                                                        .messages
                                                ).length > 0 ? (
                                                    Object.entries(
                                                        globalData.chats[chat]
                                                            .messages
                                                    ).map((message) => (
                                                        <div
                                                            key={
                                                                message.content
                                                            }
                                                            className="mb-4 grid grid-cols-[25px_1fr] items-start pb-1 last:mb-0 last:pb-0"
                                                        >
                                                            <span className="flex h-2 w-2 translate-y-1 rounded-full bg-peach" />
                                                            <div className="space-y-1">
                                                                <p className="text-sm font-medium leading-none">
                                                                    {
                                                                        message[1]
                                                                            .user
                                                                    }
                                                                </p>
                                                                <p className="text-sm text-muted-foreground">
                                                                    {
                                                                        message[1]
                                                                            .content
                                                                    }
                                                                </p>
                                                            </div>
                                                        </div>
                                                    ))
                                                ) : (
                                                    <div>
                                                        Ready to join in on the
                                                        fun? Send an
                                                        introductory message to
                                                        get started!
                                                    </div>
                                                )}
                                                <div id="scroller"></div>
                                            </ScrollArea>
                                        </CardContent>
                                        <CardContent className="w-full"></CardContent>
                                    </Card>
                                </div>
                            </CarouselItem>
                        ))}
                    </CarouselContent>
                    <CarouselPrevious />
                    <CarouselNext />
                    <Form {...form} className="w-full">
                        <form
                            onSubmit={form.handleSubmit(onSubmit)}
                            className="space-y-6"
                        >
                            <FormField
                                key="message"
                                control={form.control}
                                name="message"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormControl>
                                            <Textarea
                                                placeholder="Hi! I'm wondering if you guys are interested in going with me..."
                                                className="resize-none"
                                                {...field}
                                            />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                            <div className="flex justify-between">
                                <FormField
                                    key="chat"
                                    control={form.control}
                                    name="chat"
                                    render={({ field }) => (
                                        <FormItem className="flex flex-col">
                                            <Select
                                                onValueChange={field.onChange}
                                                defaultValue={field.value}
                                            >
                                                <FormControl>
                                                    <SelectTrigger>
                                                        <SelectValue placeholder="Chat" />
                                                    </SelectTrigger>
                                                </FormControl>
                                                <SelectContent>
                                                    {subscribedChats.map(
                                                        (chat) => (
                                                            <SelectItem
                                                                value={chat}
                                                            >
                                                                {chat}
                                                            </SelectItem>
                                                        )
                                                    )}
                                                </SelectContent>
                                            </Select>
                                        </FormItem>
                                    )}
                                />
                                <Button
                                    type="submit"
                                    className="w-3/5 bg-peach"
                                >
                                    Send {":)"}
                                </Button>
                            </div>
                        </form>
                    </Form>
                </Carousel>
            </div>
        </Background>
    );
}
