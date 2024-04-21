import React, { useState, useEffect } from "react";
import { initializeApp } from "firebase/app";
import { getDatabase, ref, onValue } from "firebase/database";
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
import { Textarea } from "./../ui/textarea";
import { ScrollArea } from "../ui/scroll-area";

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
    const [globalData, setGlobalData] = useState({});

    useEffect(() => {
        const unsubscribe = subscribedChats.map((chat) => {
            const chatRef = ref(database, `chats/${chat}`);
            return onValue(chatRef, (snapshot) => {
                setGlobalData((prevData) => ({
                    ...prevData,
                    [chat]: snapshot.val(),
                }));
            });
        });

        return () => {
            // Unsubscribe from Firebase listeners when component unmounts
            unsubscribe.forEach((unsubscribeFn) => unsubscribeFn());
        };
    }, []);

    return (
        <div className="flex justify-center w-screen h-4/5 py-10">
            <Chats data={globalData} />
        </div>
    );
}

function Chats(props) {
    const { data } = props;

    return (
        <Carousel className="max-w-xs">
            <CarouselContent>
                {subscribedChats.map((chat) => (
                    <CarouselItem key={chat} className="flex flex-col">
                        <div className="p-1">
                            <Card>
                                <CardHeader>
                                    <CardTitle>Chat #{chat}</CardTitle>
                                </CardHeader>
                                <CardContent className="flex flex-col w-full aspect-square justify-start p-6">
                                    <ScrollArea>
                                        {data[chat] &&
                                        data[chat].messages &&
                                        data[chat].messages.length > 0 ? (
                                            data[chat].messages.map(
                                                (message) => (
                                                    <div
                                                        key={message}
                                                        className="flex justify-items-start text-sm"
                                                    >
                                                        <div className="px-4 text-black">
                                                            user: {message.user}
                                                        </div>
                                                        <div className="text-slate-600">
                                                            message:{" "}
                                                            {message.content}
                                                        </div>
                                                    </div>
                                                )
                                            )
                                        ) : (
                                            <div>
                                                No messages found for this chat
                                            </div>
                                        )}
                                    </ScrollArea>
                                </CardContent>
                                <CardFooter>
                                    <Textarea />
                                </CardFooter>
                            </Card>
                        </div>
                    </CarouselItem>
                ))}
            </CarouselContent>
            <CarouselPrevious />
            <CarouselNext />
        </Carousel>
    );
}
