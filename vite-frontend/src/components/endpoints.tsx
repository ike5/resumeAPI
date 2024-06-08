/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/dPBWaqppnfX
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */

/** Add fonts into your Next.js project:

 import { Inter } from 'next/font/google'

 inter({
 subsets: ['latin'],
 display: 'swap',
 })

 To read more about using these font, please visit the Next.js documentation:
 - App Directory: https://nextjs.org/docs/app/building-your-application/optimizing/fonts
 - Pages Directory: https://nextjs.org/docs/pages/building-your-application/optimizing/fonts
 **/
export function Endpoints() {
    return (
        <div className="bg-gray-100 dark:bg-gray-800 p-6 rounded-lg ">
            <div className="mb-6">
                <h2 className="text-2xl font-bold mb-2">Fetch Ike's Resume Using API Endpoints</h2>
                <pre className="bg-gray-200 dark:bg-gray-700 p-4 rounded-md">
                    <code className="text-gray-800 dark:text-gray-200">curl -X GET "https://api.example.com/resume" -H "accept: application/json"</code>
                </pre>
            </div>
            <div>
                <h2 className="text-2xl font-bold mb-4">API Endpoints</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div className="bg-white dark:bg-gray-700 p-4 rounded-md shadow-sm">
                        <h3 className="text-lg font-bold mb-2">Get Resume</h3>
                        <p className="text-gray-600 dark:text-gray-400 mb-2">Fetch the Ike's entire resume.</p>
                        <div className="flex items-center mb-2">
                            <span
                                className="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-medium mr-2">GET</span>
                            <span className="text-gray-600 dark:text-gray-400">/resume</span>
                        </div>
                        <div className="flex items-center">
                            <span
                                className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-xs font-medium mr-2">Response</span>
                            <span className="text-gray-600 dark:text-gray-400">200 OK - application/json</span>
                        </div>
                    </div>


                    <div className="bg-white dark:bg-gray-700 p-4 rounded-md shadow-sm">
                        <h3 className="text-lg font-bold mb-2">Get Certifications</h3>
                        <p className="text-gray-600 dark:text-gray-400 mb-2">Fetch the Ike's certification history.</p>
                        <div className="flex items-center mb-2">
                            <span
                                className="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-medium mr-2">GET</span>
                            <span className="text-gray-600 dark:text-gray-400">/certs</span>
                        </div>
                        <div className="flex items-center">
                            <span
                                className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-xs font-medium mr-2">Response</span>
                            <span className="text-gray-600 dark:text-gray-400">200 OK - application/json</span>
                        </div>
                    </div>

                    <div className="bg-white dark:bg-gray-700 p-4 rounded-md shadow-sm">
                        <h3 className="text-lg font-bold mb-2">Get OS</h3>
                        <p className="text-gray-600 dark:text-gray-400 mb-2">Fetch operating systems that Ike is
                            familiar with.</p>
                        <div className="flex items-center mb-2">
                            <span
                                className="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-medium mr-2">GET</span>
                            <span className="text-gray-600 dark:text-gray-400">/os</span>
                        </div>
                        <div className="flex items-center">
                            <span
                                className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-xs font-medium mr-2">Response</span>
                            <span className="text-gray-600 dark:text-gray-400">200 OK - application/json</span>
                        </div>
                    </div>

                </div>

                <h2 className="text-2xl font-bold mb-4 my-4">Fun Facts Endpoints</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">


                    <div className="bg-white dark:bg-gray-700 p-4 rounded-md shadow-sm">
                        <h3 className="text-lg font-bold mb-2">Get Books</h3>
                        <p className="text-gray-600 dark:text-gray-400 mb-2">Fetch Ike's favorite books.</p>
                        <div className="flex items-center mb-2">
                            <span
                                className="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-medium mr-2">GET</span>
                            <span className="text-gray-600 dark:text-gray-400">/books</span>
                        </div>
                        <div className="flex items-center">
                            <span
                                className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-xs font-medium mr-2">Response</span>
                            <span className="text-gray-600 dark:text-gray-400">200 OK - application/json</span>
                        </div>
                    </div>
                    <div className="bg-white dark:bg-gray-700 p-4 rounded-md shadow-sm">
                        <h3 className="text-lg font-bold mb-2">Get Books</h3>
                        <p className="text-gray-600 dark:text-gray-400 mb-2">Fetch Ike's favorite books.</p>
                        <div className="flex items-center mb-2">
                            <span
                                className="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-medium mr-2">GET</span>
                            <span className="text-gray-600 dark:text-gray-400">/books</span>
                        </div>
                        <div className="flex items-center">
                            <span
                                className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-xs font-medium mr-2">Response</span>
                            <span className="text-gray-600 dark:text-gray-400">200 OK - application/json</span>
                        </div>
                    </div>
                    <div className="bg-white dark:bg-gray-700 p-4 rounded-md shadow-sm">
                        <h3 className="text-lg font-bold mb-2">Get Books</h3>
                        <p className="text-gray-600 dark:text-gray-400 mb-2">Fetch Ike's favorite books.</p>
                        <div className="flex items-center mb-2">
                            <span
                                className="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-medium mr-2">GET</span>
                            <span className="text-gray-600 dark:text-gray-400">/books</span>
                        </div>
                        <div className="flex items-center">
                            <span
                                className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-xs font-medium mr-2">Response</span>
                            <span className="text-gray-600 dark:text-gray-400">200 OK - application/json</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
