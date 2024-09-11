# GroupDoodles-server
Group-doodles is a collaborative drawing application built with Django, designed to bring together artists and doodlers in a shared creative space.

## Overview
Group-doodles provides a platform where users can create, share, and collaborate on digital drawings. The app combines the fun of casual doodling with the power of group creativity, allowing multiple users to contribute to a single piece of art.

## Key Features

Collaborative Drawing: Users can create new drawings or join existing ones, working together in real-time to create unique artworks.
User Profiles: Each user has a profile where they can showcase their contributions and favorite pieces.
Color Palette System: Users can create and save custom color palettes, making it easy to maintain a consistent style across multiple drawings.
Drawing Management: Create, edit, and delete drawings. Users can also browse through a gallery of all public drawings.
Version History: Each drawing maintains a history of changes, allowing users to review the evolution of the artwork or revert to previous versions.
Social Features: Users can like, comment on, and share drawings, fostering a community of artists and enthusiasts.

## How It Works

Sign Up and Profile Creation: New users can create an account and set up their profile, customizing their avatar and bio.
Start or Join a Drawing: Users can initiate a new drawing or browse existing ones to join.
Drawing Interface: The main drawing interface provides a canvas where users can doodle using various tools (pencil, brush, eraser, etc.) and choose colors from the palette.
Real-time Collaboration: When multiple users work on the same drawing, changes are synchronized in real-time, allowing for true collaborative creation.
Save and Share: Completed drawings can be saved, shared on the platform, or exported for use elsewhere.
Explore and Interact: Users can browse the gallery of public drawings, leave comments, and like their favorite pieces.

## Technical Details

Built with Django, leveraging its robust ORM for managing complex data relationships
Uses PostgreSQL for efficient data storage and retrieval
Implements WebSocket technology for real-time drawing updates
Responsive design ensures a seamless experience across desktop and mobile devices

## Models
The application is structured around four main models:

Users: Stores user account information and preferences.
Drawings: Represents individual drawing projects, including metadata and content.
Color: Defines individual colors that can be used in drawings.
Palettes: Groups colors into reusable palettes that users can save and share.
