from array import *
w = f"\033[0;97;1m"
r = f"\033[2;91;1m"
gry = f"\033[37m"
green = '\033[32m'
reset = '\033[0m'
bold = "\033[1m"
def calculate_time(total_distance): 
    minutes = total_distance * 10
    return f"{round(minutes/60, 2)} hours"
def get_route(roads_distances,current_loc, destination, answered_questions):
    if answered_questions == 6: cockfighting_arena = "Cockfighting Arena"
    else: cockfighting_arena = "????????"
    if current_loc == 1:
        if destination == 2:
            #routes = ["2 5 3 1", "2 5 6 4", "2 5 8 11"]
            #routes = [[eval(f"roads_distances[{distance}]")  for distance in routes[0].split()], [eval(f"roads_distances[{distance}]")  for distance in routes[1].split()], [eval(f"roads_distances[{distance}]") for distance in routes[2].split()]]
            route1 = [roads_distances[2],roads_distances[5],roads_distances[3],roads_distances[1]]
            route2 = [roads_distances[2],roads_distances[5],roads_distances[6],roads_distances[4]]
            route3 = [roads_distances[2],roads_distances[5],roads_distances[8],roads_distances[11],roads_distances[9],roads_distances[4]]
            routes = [eval("+".join(list(map(str,route1)))),eval("+".join(list(map(str,route2)))),eval("+".join(list(map(str,route3))))]
            route1_asString = f" Double Shot → Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[0])}m{reset}"
            route2_asString = f" Double Shot → Fountain → Hammer Swing → Pirate Ship = {r}{str(routes[1])}m{reset}"
            route3_asString = f" Double Shot → Fountain → Entrance → Carousel → Hammer Swing → Pirate Ship = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n"+"\n".join([route1_asString,route2_asString,route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i  in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i+1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}",final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["3 6 4 2", "3 6 7 5", "3 6 9 12 10 5" ][routes.index(best_route_distance)]
            return list(map(int,roads_to_remove_zombies.split()))
        elif destination == 3:
            print(f"{r}\nALL ROUTES:{reset}\n Double Shot = {roads_distances[2]}m")
            print(f"{r}\nBEST ROUTE: {reset}Double Shot = {roads_distances[2]}m")
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(roads_distances[2])}")
            return[3]
        elif destination == 4:
            route1 = [roads_distances[2], roads_distances[5]]
            routes = [eval("+".join(list(map(str, route1))))]
            route1_asString = f"Double Shot → Fountain  = {r}{str(routes[0])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n" f"{route1_asString}")
            best_route_distance = min(routes)
            print(f"{r}\nBEST ROUTE: {reset}", eval(f"route{routes.index(best_route_distance) + 1}_asString"))
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["3 6"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 5:
            route1 = [roads_distances[2], roads_distances[5], roads_distances[6]]
            route2 = [roads_distances[2], roads_distances[5], roads_distances[3], roads_distances[1],roads_distances[4]]
            route3 = [roads_distances[2], roads_distances[5], roads_distances[8], roads_distances[11], roads_distances[9]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Double Shot → Fountain → Hammer Swing = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → {cockfighting_arena} → Pirate Ship → Hammer Swing = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Double Shot → Fountain → Entrance → Carousel → Hammer Swing = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["3 6 7", "3 6 4 2 5", "3 6 9 12 10"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 6:
            route1 = [roads_distances[2], roads_distances[7]]
            route2 = [roads_distances[2], roads_distances[5], roads_distances[8], roads_distances[10]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Double Shot → Ferris Wheel = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → Entrance → Ferris Wheel = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["3 8", "3 6 9 11"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 7:
            route1 = [roads_distances[2], roads_distances[5], roads_distances[8]]
            routes = [eval("+".join(list(map(str, route1))))]
            route1_asString = f"Double Shot → Fountain → Entrance = {r}{str(routes[0])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString]))
            best_route_distance = min(routes)
            print(f"{r}\nBEST ROUTE: {reset}", eval(f"route{routes.index(best_route_distance) + 1}_asString"))
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["3 6 9"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 8:
            route1 = [roads_distances[2], roads_distances[5], roads_distances[6], roads_distances[9]]
            route2 = [roads_distances[2], roads_distances[5], roads_distances[8], roads_distances[11]]
            route3 = [roads_distances[2], roads_distances[5], roads_distances[3], roads_distances[1],roads_distances[4], roads_distances[9]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3))))]
            route1_asString = f"Double Shot → Fountain → Hammer Swing → Carousel = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → Entrance → Carousel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Double Shot → Fountain → {cockfighting_arena} → Pirate Ship → Hammer Swing → Carousel  = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["3 6 7 10", "3 6 9 12", "3 6 4 2 5 10"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 9:
            route1 = [roads_distances[2], roads_distances[5], roads_distances[3]]
            route2 = [roads_distances[2], roads_distances[5], roads_distances[8], roads_distances[11],roads_distances[9], roads_distances[6], roads_distances[3]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Double Shot → Fountain = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → Entrance → Carousel → Hammer Swing → Fountain → {cockfighting_arena} = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            return
    elif current_loc == 2:
        if destination == 1:
            route1 = [roads_distances[4], roads_distances[6], roads_distances[5], roads_distances[2]]
            route2 = [roads_distances[4], roads_distances[6], roads_distances[3], roads_distances[0]]
            route3 = [roads_distances[4], roads_distances[6], roads_distances[8], roads_distances[10],roads_distances[7], roads_distances[2]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),
                      eval("+".join(list(map(str, route3))))]
            route1_asString = f"Hammer Swing → Fountain → Double Shot → Roller Coaster = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Hammer Swing → Fountain → REntrance → Ferris Wheel → Double Shot → Roller Coaster = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["5 7 6 3", "5 7 4 1", "5 7 9 11 8 3"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 3:
            route1 = [roads_distances[4], roads_distances[6], roads_distances[5]]
            route2 = [roads_distances[4], roads_distances[6], roads_distances[3], roads_distances[0]]
            route3 = [roads_distances[4], roads_distances[6], roads_distances[8], roads_distances[10],roads_distances[7]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3))))]
            route1_asString = f"Hammer Swing → Fountain → Double Shot = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster → Double Shot = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Hammer Swing → Fountain → Entrance → Ferris Wheel → Double Shot = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["5 7 6", "5 7 4 1", "5 7 9 11 8"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 4:
            route1 = [roads_distances[4], roads_distances[6]]
            routes = [eval("+".join(list(map(str, route1))))]
            route1_asString = f"Hammer Swing → Fountain = {r}{str(routes[0])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n" f"{route1_asString}")
            best_route_distance = min(routes)
            print(f"{r}\nBEST ROUTE: {reset}", eval(f"route{routes.index(best_route_distance) + 1}_asString"))
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["5 7"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 5:
            print(f"{r}\nALL ROUTES:{reset}\n Hammer Swing = {roads_distances[4]}m")
            print(f"{r}\nBEST ROUTE: {reset}Hammer Swing = {roads_distances[4]}m")
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(roads_distances[4])}")
            return [5]
        elif destination == 6: #----------------------------------------------------------------------------------------------------  dito ka na magsimula
            route1 = [roads_distances[4], roads_distances[6], roads_distances[5], roads_distances[7]]
            route2 = [roads_distances[4], roads_distances[6], roads_distances[8], roads_distances[10]]
            route3 = [roads_distances[4], roads_distances[6], roads_distances[3], roads_distances[0], roads_distances[2], roads_distances[7]]
            route4 = [roads_distances[4], roads_distances[6], roads_distances[3], roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[8], roads_distances[10]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4))))]
            route1_asString = f"Hammer Swing → Fountain → Double Shot → Ferris Wheel = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → Entrance → Ferris Wheel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Ferris Wheel = {r}{str(routes[2])}m{reset}"
            route4_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Fountain → Entrance → Ferris Wheel = {r}{str(routes[3])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["5 7 6 8", "5 7 9 11", "5 7 4 1 3 8", "5 7 4 1 3 6 9 11"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 7:
            route1 = [roads_distances[4], roads_distances[6], roads_distances[8]]
            route2 = [roads_distances[4], roads_distances[6], roads_distances[3], roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[8]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Hammer Swing → Fountain → Entrance = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Fountain → Entrance = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["5 7 9", "5 7 4 1 3 6 9"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 8:
            route1 = [roads_distances[4], roads_distances[9]]
            route2 = [roads_distances[4], roads_distances[6], roads_distances[8], roads_distances[11]]
            route3 = [roads_distances[4], roads_distances[6], roads_distances[3], roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[8], roads_distances[11]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Hammer Swing → Carousel  = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → Entracne → Carousel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Fountain → Entrance → Carousel  = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["5 10", "5 7 9 12", "5 7 4 1 3 6 9 12"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 9:
            route1 = [roads_distances[4], roads_distances[6], roads_distances[3]]
            route2 = [roads_distances[4], roads_distances[6], roads_distances[8], roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[3]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Hammer Swing → Fountain → {cockfighting_arena} = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → Entrance → Ferris Wheel → Double Shot → Fountain → {cockfighting_arena} = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            return
    elif current_loc == 3:
        if destination == 1:
            route1 = [roads_distances[2]]
            route2 = [roads_distances[5], roads_distances[3], roads_distances[0]]
            route3 = [roads_distances[5], roads_distances[8], roads_distances[11], roads_distances[9],roads_distances[6], roads_distances[3],roads_distances[0]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Roller Coaster = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → {cockfighting_arena} → Roller Coaster = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → Entrance → Carousel → Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["3", "6 4 1", "6 9 12 10 7 4 1"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 2:
            route1 = [roads_distances[5],roads_distances[6], roads_distances[4]]
            route2 = [roads_distances[5], roads_distances[3], roads_distances[1]]
            route3 = [roads_distances[5], roads_distances[8], roads_distances[11], roads_distances[9],roads_distances[4]]
            route4 = [roads_distances[5], roads_distances[8], roads_distances[11], roads_distances[9],roads_distances[6], roads_distances[3], roads_distances[1]]
            routes = [eval("+".join(list(map(str, route1)))),eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3)))),eval("+".join(list(map(str, route4))))]
            route1_asString = f"Fountain → Hammer Swing → Pirate Ship = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → Entrance → Carousel → Hammer Swing → Pirate Ship = {r}{str(routes[2])}m{reset}"
            route4_asString = f"Fountain → Entrance → Carousel → Hammer Swing → Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[3])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString,route4_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["6 7 5", "6 4 2", "6 9 12 10 5", "6 9 12 10 7 4 2"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 4:
            print(f"{r}\nALL ROUTES:{reset}\n Fountain = {roads_distances[5]}m")
            print(f"{r}\nBEST ROUTE: {reset}Fountain = {roads_distances[5]}m")
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(roads_distances[5])}")
            return [6]
        elif destination == 5:
            route1 = [roads_distances[5], roads_distances[6]]
            route2 = [roads_distances[5], roads_distances[3], roads_distances[1],roads_distances[4]]
            route3 = [roads_distances[5], roads_distances[8], roads_distances[11], roads_distances[9]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Fountain → Hammer Swing = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → {cockfighting_arena} → Pirate Ship → Hammer Swing = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → Entrance → Carousel → Hammer Swing = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["6 7", "6 4 2 5", "6 9 12 10"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 6:
            route1 = [roads_distances[7]]
            route2 = [roads_distances[5], roads_distances[8], roads_distances[10]]
            route3 = [roads_distances[5], roads_distances[3], roads_distances[1], roads_distances[4],roads_distances[6], roads_distances[8], roads_distances[10]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Ferris Wheel  = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → Entrance → Ferris Wheel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → {cockfighting_arena} → Pirate Ship → Hammer Swing → Fountain → Entrance → Ferris Wheel = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["8", "6 9 11", "6 4 2 5 7 9 11"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 7:
            route1 = [roads_distances[5],roads_distances[8]]
            route2 = [roads_distances[5], roads_distances[3], roads_distances[1],roads_distances[4],roads_distances[6],roads_distances[8]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Fountain → Entrance  = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → {cockfighting_arena} → Pirate Ship → Hammer Swing → Fountain → Entrance = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["6 9", "6 4 2 5 7 9"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 8:
            route1 = [roads_distances[5], roads_distances[6], roads_distances[9]]
            route2 = [roads_distances[5], roads_distances[8], roads_distances[11]]
            route3 = [roads_distances[5], roads_distances[3], roads_distances[1], roads_distances[4],roads_distances[9]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Fountain → Hammer Swing → Carousel   = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → Entrance → Carousel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → {cockfighting_arena} →  Pirate Ship → Hammer Swing → Carousel = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["6 7 10", "6 9 12", "6 4 2 5 10"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 9:
            route1 = [roads_distances[5], roads_distances[3]]
            route2 = [roads_distances[5], roads_distances[8], roads_distances[11],roads_distances[9], roads_distances[6], roads_distances[3]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Fountain → {cockfighting_arena}  = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → Entrance → Carousel → Hammer Swing → Fountain → {cockfighting_arena}  = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            return
    elif current_loc == 4:
        if destination == 1:
            route1 = [roads_distances[5], roads_distances[2]]
            route2 = [roads_distances[3], roads_distances[0]]
            route3 = [roads_distances[8], roads_distances[10], roads_distances[7], roads_distances[2]]
            route4 = [roads_distances[8], roads_distances[10], roads_distances[7], roads_distances[5],roads_distances[3], roads_distances[0]]
            route5 = [roads_distances[8], roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),eval("+".join(list(map(str, route5))))]
            route1_asString = f"Double Shot → Roller Coaster  = {r}{str(routes[0])}m{reset}"
            route2_asString = f"{cockfighting_arena} → Roller Coaster = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Entrance → Ferris Wheel → Double Shot → Roller Coaster = {r}{str(routes[2])}m{reset}"
            route4_asString = f"Entrance → Ferris Wheel → Double Shot → Fountain → {cockfighting_arena} → Roller Coaster = {r}{str(routes[3])}m{reset}"
            route5_asString = f"Entrance → Carousel → Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster = {r}{str(routes[4])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString,route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["6 3", "4 1", "9 11 8 3", "9 11 8 6 4 1", "9 12 10 7 4 1" ][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 2:
            route1 = [roads_distances[3], roads_distances[1]]
            route2 = [roads_distances[6], roads_distances[4]]
            route3 = [roads_distances[8], roads_distances[11], roads_distances[9], roads_distances[4]]
            route4 = [roads_distances[8], roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[3], roads_distances[1]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4))))]
            route1_asString = f"{cockfighting_arena} → Pirate Ship  = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Pirate Ship = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Entrance → Carousel → Hammer Swing → Pirate Ship = {r}{str(routes[2])}m{reset}"
            route4_asString = f"Entrance → Ferris Wheel → Double Shot → Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[3])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["4 2", "7 5", "9 12 10 5", "9 11 8 6 4 2",][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 3:
            route1 = [roads_distances[5]]
            route2 = [roads_distances[3], roads_distances[0],roads_distances[2]]
            route3 = [roads_distances[8], roads_distances[10], roads_distances[7]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Double Shot  = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → Roller Coaster → Double Shot = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Entrance → Ferris Wheel → Double Shot = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["6", "4 1 3", "9 11 8", ][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 5:
            route1 = [roads_distances[6]]
            route2 = [roads_distances[3], roads_distances[1], roads_distances[4]]
            route3 = [roads_distances[8], roads_distances[11], roads_distances[9]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Hammer Swing = {r}{str(routes[0])}m{reset}"
            route2_asString = f"{cockfighting_arena} → Pirate Ship → Hammer Swing  = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Entrance → Carousel → Hammer Swing = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["7", "4 2 5", "9 12 10", ][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 6:
            route1 = [roads_distances[8], roads_distances[10]]
            route2 = [roads_distances[5], roads_distances[7]]
            route3 = [roads_distances[3], roads_distances[0], roads_distances[2], roads_distances[7]]
            route4 = [roads_distances[8], roads_distances[11], roads_distances[9], roads_distances[6],roads_distances[3], roads_distances[0],roads_distances[2],roads_distances[7]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4))))]
            route1_asString = f"Entrance → Ferris Wheel = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Ferris Wheel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"{cockfighting_arena} → Roller Coaster → Double Shot → Ferris Wheel = {r}{str(routes[2])}m{reset}"
            route4_asString = f"Entrance → Carousel → Hammer Swing → Fountain → {cockfighting_arena}→ Roller Coaster → Double Shot → Ferris Wheel = {r}{str(routes[3])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["9 11", "6 8", "4 1 3 8", "9 12 10 7 4 1 3 8", ][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 7:
            route1 = [roads_distances[8]]
            route2 = [roads_distances[3], roads_distances[0], roads_distances[2],roads_distances[5], roads_distances[8]]
            route3 = [roads_distances[3], roads_distances[1], roads_distances[4],roads_distances[6], roads_distances[8]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Entrance = {r}{str(routes[0])}m{reset}"
            route2_asString = f"{cockfighting_arena} → Roller Coaster → Double Shot → Fountain → Entrance = {r}{str(routes[1])}m{reset}"
            route3_asString = f"{cockfighting_arena} → Pirate Ship → Hammer Swing → Fountain → Entrance = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["9", "4 1 3 6 9", "4 2 5 7 9", ][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 8:
            route1 = [roads_distances[8], roads_distances[11]]
            route2 = [roads_distances[6], roads_distances[9]]
            route3 = [roads_distances[3], roads_distances[1], roads_distances[4], roads_distances[9]]
            route4 = [roads_distances[3], roads_distances[1], roads_distances[4], roads_distances[6],roads_distances[8], roads_distances[11]]
            route5 = [roads_distances[3], roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[8], roads_distances[11]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),eval("+".join(list(map(str, route5))))]
            route1_asString = f"Entrance → Carousel  = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Carousel  = {r}{str(routes[1])}m{reset}"
            route3_asString = f"{cockfighting_arena} → Pirate Ship → Hammer Swing → Carousel = {r}{str(routes[2])}m{reset}"
            route4_asString = f"{cockfighting_arena} → Pirate Ship → Hammer Swing → Fountain → Entrance → Carousel = {r}{str(routes[3])}m{reset}"
            route5_asString = f"{cockfighting_arena} → Roller Coaster → Double Shot → Fountain → Entrance → Carousel = {r}{str(routes[4])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString,route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}") 
            roads_to_remove_zombies = ["9 12", "7 10", "4 2 5 10", "4 2 5 7 9 12", "4 1 3 6 9 12" ][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 9:
            print(f"{r}\nALL ROUTES:{reset}\nFountain = {roads_distances[3]}m")
            print(f"{r}\nBEST ROUTE: {reset}Fountain = {roads_distances[3]}m")
            print(f"{r}\nEstimated Time of Arrival:{reset} {calculate_time(roads_distances[3])}") 
            return 
    elif current_loc == 5:
        if destination == 1:
            route1 = [roads_distances[6],roads_distances[5],roads_distances[2]]
            route2 = [roads_distances[6], roads_distances[3], roads_distances[0]]
            route3 = [roads_distances[6], roads_distances[8], roads_distances[10], roads_distances[7], roads_distances[2]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Fountain → Double Shot → Roller Coaster = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → {cockfighting_arena} → Roller Coaster = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → Entrance → Ferris Wheel → Double Shot → Roller Coaster = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["7 6 3", "7 4 1", "7 9 11 8 3", ][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 2:
            route1 = [roads_distances[4]]
            route2 = [roads_distances[6], roads_distances[3], roads_distances[1]]
            route3 = [roads_distances[6], roads_distances[8], roads_distances[10],roads_distances[7], roads_distances[5], roads_distances[1]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Pirate Ship = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → Entrance → Ferris Wheel → Double Shot → Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["5", "7 4 2", "7 9 11 8 6 4 2", ][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 3:
            route1 = [roads_distances[6],roads_distances[5]]
            route2 = [roads_distances[6], roads_distances[3], roads_distances[0], roads_distances[2]]
            route3 = [roads_distances[6], roads_distances[8], roads_distances[10],roads_distances[7]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Fountain → Double Shot = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → {cockfighting_arena} → Roller Coaster → Double Shot = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → Entrance → Ferris Wheel → Double Shot = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["7 6", "7 4 1 3", "7 9 11 8"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 4: # 1 route
            print(f"{r}\nALL ROUTES:{reset}\nFountain = {roads_distances[6]}m")
            print(f"{r}\nBEST ROUTE: {reset}Fountain = {roads_distances[6]}m")
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(roads_distances[6])}")
            return[7]
        elif destination == 6:
            route1 = [roads_distances[6], roads_distances[5],roads_distances[7]]
            route2 = [roads_distances[6], roads_distances[8], roads_distances[10]]
            route3 = [roads_distances[6], roads_distances[3], roads_distances[0], roads_distances[2],roads_distances[7]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Fountain → Double Shot → Ferris Wheel = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → Entrance → Ferris Wheel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Ferris Wheel = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["7 6 8","7 9 11","7 4 1 3 8"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 7:
            route1 = [roads_distances[6], roads_distances[8]]
            route2 = [roads_distances[6], roads_distances[3], roads_distances[0],roads_distances[2],roads_distances[5],roads_distances[8]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Fountain → Entrance = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Fountain → Entrance = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["7 9", "7 4 1 3 6 9"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 8:
            route1 = [roads_distances[9]]
            route2 = [roads_distances[6], roads_distances[8], roads_distances[11]]
            route3 = [roads_distances[6], roads_distances[3], roads_distances[0], roads_distances[2], roads_distances[5],roads_distances[8],roads_distances[11]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Carousel = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → Entrance → Carousel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Fountain → Entrance → Carousel = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["10", "7 9 12", "7 4 1 3 6 9 12"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 9:
            route1 = [roads_distances[6], roads_distances[3]]
            route2 = [roads_distances[6], roads_distances[8], roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[3]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Fountain → {cockfighting_arena} = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Fountain → Entrance → Ferris Wheel → Double Shot → Fountain → {cockfighting_arena} = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            return
    elif current_loc == 6:
        if destination == 1:
            route1 = [roads_distances[7],roads_distances[2]]
            route2 = [roads_distances[7], roads_distances[6], roads_distances[3], roads_distances[0]]
            route3 = [roads_distances[7], roads_distances[5], roads_distances[8], roads_distances[11],roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3))))]
            route1_asString = f"Double Shot → Roller Coaster = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → {cockfighting_arena} → Roller Coaster = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Double Shot → Fountain → Entrance → Carousel → Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["8 3", "8 6 4 1", "8 6 9 12 10 7 4 1"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 2:
            route1 = [roads_distances[7], roads_distances[5], roads_distances[3], roads_distances[1]]
            route2 = [roads_distances[7], roads_distances[5], roads_distances[6], roads_distances[4]]
            route3 = [roads_distances[7], roads_distances[5], roads_distances[8], roads_distances[11],roads_distances[9], roads_distances[4]]
            route4 = [roads_distances[7], roads_distances[5], roads_distances[8], roads_distances[11],roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[1]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4))))]
            route1_asString = f"Double Shot → Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → Hammer Swing → Pirate Ship = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Double Shot → Fountain → Entrance → Carousel → Hammer Swing → Pirate Ship = {r}{str(routes[2])}m{reset}"
            route4_asString = f"Double Shot → Fountain → Entrance → Carousel → Hammer Swing → Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[3])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["8 6 4 2 ", "8 6 7 5", "8 6 9 12 10 5", "8 6 9 12 10 7 4 2"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 3:
            print(f"{r}\nALL ROUTES:{reset}\n Double Shot = {roads_distances[7]}m")
            print(f"{r}\nBEST ROUTE: {reset}Double Shot = {roads_distances[7]}m")
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(roads_distances[7])}")
            return [8]
        elif destination == 4:
            route1 = [roads_distances[7], roads_distances[5]]
            routes = [eval("+".join(list(map(str, route1))))]
            route1_asString = f"Double Shot → Fountain = {r}{str(routes[0])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString]))
            best_route_distance = min(routes)
            print(f"{r}\nBEST ROUTE: {reset}", eval(f"route{routes.index(best_route_distance) + 1}_asString"))
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            return [8,6]
        elif destination == 5:
            route1 = [roads_distances[7], roads_distances[5], roads_distances[6]]
            route2 = [roads_distances[7], roads_distances[5], roads_distances[3], roads_distances[1], roads_distances[4]]
            route3 = [roads_distances[7], roads_distances[5], roads_distances[8], roads_distances[11],roads_distances[9]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3))))]
            route1_asString = f"Double Shot → Fountain → Hammer Swing = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → {cockfighting_arena} → Pirate Ship → Hammer Swing = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Double Shot → Fountain → Entrance → Carousel → Hammer Swing  = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["8 6 7", "8 6 4 2 5", "8 6 9 12 10"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 7:
            route1 = [roads_distances[7], roads_distances[5], roads_distances[8]]
            route2 = [roads_distances[7], roads_distances[5], roads_distances[3], roads_distances[1], roads_distances[4], roads_distances[6], roads_distances[8]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Double Shot → Fountain → Entrance = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → {cockfighting_arena} → Pirate Ship → Hammer Swing → Fountain → Entrance = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["8 6 9", "8 6 4 2 5 7 9"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 8:
            route1 = [roads_distances[7], roads_distances[5], roads_distances[6], roads_distances[9]]
            route2 = [roads_distances[7], roads_distances[5], roads_distances[8], roads_distances[11]]
            route3 = [roads_distances[7], roads_distances[5], roads_distances[3], roads_distances[1],roads_distances[4], roads_distances[9]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3))))]
            route1_asString = f"Double Shot → Fountain → Hammer Swing → Carousel = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → Entrance → Carousel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Double Shot → Fountain → {cockfighting_arena} → Pirate Ship → Hammer Swing → Carousel = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["8 6 7 10", "8 6 9 12", "8 6 4 2 5 10"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 9:
            route1 = [roads_distances[7], roads_distances[5], roads_distances[3]]
            route2 = [roads_distances[7], roads_distances[5], roads_distances[8], roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[3]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Double Shot → Fountain → {cockfighting_arena} = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Double Shot → Fountain → Entrance → Carousel → Hammer Swing → Fountain → {cockfighting_arena}= {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            return
    elif current_loc == 7:
        if destination == 1:
            route1 = [roads_distances[8], roads_distances[5], roads_distances[2]]
            route2 = [roads_distances[10], roads_distances[7], roads_distances[2]]
            route3 = [roads_distances[8], roads_distances[3], roads_distances[0]]
            route4 = [roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[3], roads_distances[0]]
            route5 = [roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[5], roads_distances[2]]
            route6 = [roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                      eval("+".join(list(map(str, route5)))), eval("+".join(list(map(str, route6))))]
            route1_asString = f"Fountain → Double Shot → Roller Coaster = {r}{str(routes[0])}{reset}"
            route2_asString = f"Ferris Wheel → Double Shot → Roller Coaster = {r}{str(routes[1])}{reset}"
            route3_asString = f"Fountain → Cockfighting arena → Roller Coaster = {r}{str(routes[2])}{reset}"
            route4_asString = f"Ferris Wheel → Double Shot → Fountain → Cockfighting arena → Roller Coaster = {r}{str(routes[3])}{reset}"
            route5_asString = f"Carousel → Hammer Swing → Fountain → Double Shot → Roller Coaster = {r}{str(routes[0])}{reset}"
            route6_asString = f"Carousel → Hammer Swing → Fountain → Cockfighting arena → Roller Coaster = {r}{str(routes[0])}{reset}"
            print(f"{r}\ALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString, route5_asString, route6_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["9 6 3", "11 8 3", "9 4 1", "11 8 6 4 1", "12 10 7 6 3", "12 10 7 4 1"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 2:
            route1 = [roads_distances[8], roads_distances[6], roads_distances[4]]
            route2 = [roads_distances[8], roads_distances[3], roads_distances[1]]
            route3 = [roads_distances[11], roads_distances[9], roads_distances[4]]
            route4 = [roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[3], roads_distances[1]]
            route5 = [roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[6], roads_distances[4]]
            route6 = [roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[1]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),
                      eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                      eval("+".join(list(map(str, route5)))), eval("+".join(list(map(str, route6))))]
            route1_asString = f"Fountain → Hammer Swing → Pirate Ship = {r}{str(routes[0])}{reset}"
            route2_asString = f"Fountain → Cockfighting arena → Pirate Ship = {r}{str(routes[1])}{reset}"
            route3_asString = f"Carousel → Hammer Swing → Pirate Ship = {r}{str(routes[2])}{reset}"
            route4_asString = f"Ferris Wheel → Double Shot → Fountain → Cockfighting arena → Pirate Ship = {r}{str(routes[3])}{reset}"
            route5_asString = f"Ferris Wheel → Double Shot → Fountain → Hammer Swing → Pirate Ship = {r}{str(routes[0])}{reset}"
            route6_asString = f"Carousel → Hammer Swing → Fountain → Cockfighting arena → Pirate Ship = {r}{str(routes[0])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString, route5_asString, route6_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["9 7 5", "9 4 2", "12 10 5", "11 8 6 4 2", "11 8 6 7 5", "12 10 7 4 2"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 3:
            route1 = [roads_distances[8], roads_distances[5]]
            route2 = [roads_distances[10], roads_distances[7]]
            route3 = [roads_distances[8], roads_distances[3], roads_distances[0], roads_distances[2]]
            route4 = [roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[5]]
            route5 = [roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0], roads_distances[2]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),
                      eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                      eval("+".join(list(map(str, route5))))]
            route1_asString = f"Fountain → Double Shot = {r}{str(routes[0])}{reset}"
            route2_asString = f"Ferris Wheel → Double Shot = {r}{str(routes[1])}{reset}"
            route3_asString = f"Fountain → Cockfighting arena → Roller Coaster → Double Shot = {r}{str(routes[2])}{reset}"
            route4_asString = f"Carousel → Hammer Swing → Fountain → Double Shot = {r}{str(routes[3])}{reset}"
            route5_asString = f"Carousel → Hammer Swing → Fountain → Cockfighting arena → Roller Coaster → Double Shot = {r}{str(routes[0])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString, route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["9 6", "11 8", "9 4 1 3", "12 10 7 6", "12 10 7 4 1 3"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 4:
            route1 = [roads_distances[8]]
            route2 = [roads_distances[10], roads_distances[7], roads_distances[5]]
            route3 = [roads_distances[11], roads_distances[9], roads_distances[6]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Fountain = {r}{str(routes[0])}{reset}"
            route2_asString = f"Ferris Wheel → Double Shot → Fountain = {r}{str(routes[1])}{reset}"
            route3_asString = f"Carousel → Hammer Swing → Fountain = {r}{str(routes[2])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["9", "11 8 6", "12 10 7"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 5:
            route1 = [roads_distances[8], roads_distances[6]]
            route2 = [roads_distances[11], roads_distances[9]]
            route3 = [roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[6]]
            route4 = [roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[3], roads_distances[1], roads_distances[4]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),
                      eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4))))]
            route1_asString = f"Fountain → Hammer Swing = {r}{str(routes[0])}{reset}"
            route2_asString = f"Carousel → Hammer Swing = {r}{str(routes[1])}{reset}"
            route3_asString = f"Ferris Wheel → Double Shot → Fountain → Hammer Swing = {r}{str(routes[2])}{reset}"
            route4_asString = f"Ferris Wheel → Double Shot → Fountain → Cockfighting arena → Pirate Ship → Hammer Swing = {r}{str(routes[3])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} wala pa")
            roads_to_remove_zombies = ["9 7", "12 10", "11 8 6 7", "11 8 6 4 2 5"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 6:
            route1 = [roads_distances[10]]
            route2 = [roads_distances[8], roads_distances[5], roads_distances[7]]
            route3 = [roads_distances[8], roads_distances[3], roads_distances[0], roads_distances[2], roads_distances[7]]
            route4 = [roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[5], roads_distances[7]]
            route5 = [roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0], roads_distances[2], roads_distances[7]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),
                      eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                      eval("+".join(list(map(str, route5))))]
            route1_asString = f"Ferris Wheel = {r}{str(routes[0])}{reset}"
            route2_asString = f"Fountain → Double Shot → Ferris Wheel = {r}{str(routes[1])}{reset}"
            route3_asString = f"Fountain → Cockfighting arena → Roller Coaster → Double Shot → Ferris Wheel = {r}{str(routes[2])}{reset}"
            route4_asString = f"Carousel → Hammer Swing → Fountain → Double Shot → Ferris Wheel = {r}{str(routes[3])}{reset}"
            route5_asString = f"Carousel → Hammer Swing → Fountain → Cockfighting arena → Roller Coaster → Double Shot → Ferris Wheel = {r}{str(routes[0])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString, route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["11", "9 6 8", "9 4 1 3 8", "12 10 7 6 8", "12 10 7 4 1 3 8"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 8:
            route1 = [roads_distances[11]]
            route2 = [roads_distances[8], roads_distances[6], roads_distances[9]]
            route3 = [roads_distances[8], roads_distances[3], roads_distances[1], roads_distances[4], roads_distances[9]]
            route4 = [roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[6], roads_distances[9]]
            route5 = [roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[3], roads_distances[1], roads_distances[4], roads_distances[9]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),
                      eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                      eval("+".join(list(map(str, route5))))]
            route1_asString = f"Carousel = {r}{str(routes[0])}{reset}"
            route2_asString = f"Fountain → Hammer Swing → Carousel = {r}{str(routes[1])}{reset}"
            route3_asString = f"Fountain → Cockfighting arena → Pirate Ship → Hammer Swing → Carousel = {r}{str(routes[2])}{reset}"
            route4_asString = f"Ferris Wheel → Double Shot → Fountain → Hammer Swing → Carousel = {r}{str(routes[3])}{reset}"
            route5_asString = f"Ferris Wheel → Double Shot → Fountain → Cockfighting arena → Pirate Ship → Hammer Swing → Carousel = {r}{str(routes[0])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join(
                [route1_asString, route2_asString, route3_asString, route4_asString, route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["12", "9 7 10", "9 4 2 5 10", "11 8 6 7 10", "11 8 6 4 2 5 10"][
                routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 9:
            route1 = [roads_distances[8], roads_distances[3]]
            route2 = [roads_distances[10], roads_distances[7], roads_distances[5], roads_distances[3]]
            route3 = [roads_distances[11], roads_distances[9], roads_distances[6], roads_distances[3]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))), eval("+".join(list(map(str, route3))))]
            route1_asString = f"Fountain → Cockfighting arena = {r}{str(routes[0])}{reset}"
            route2_asString = f"Ferris Wheel → Double Shot → Fountain → Cockfighting arena = {r}{str(routes[1])}{reset}"
            route3_asString = f"Carousel → Hammer Swing → Fountain → Cockfighting arena = {r}{str(routes[2])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["9 4", "11 8 6 4", "12 10 7 4"][routes.index(best_route_distance)]
            return
    elif current_loc == 8:
        if destination == 1:
            route1 = [roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0]]
            route2 = [roads_distances[9], roads_distances[6], roads_distances[5], roads_distances[2]]
            route3 = [roads_distances[9], roads_distances[6], roads_distances[8], roads_distances[10],roads_distances[7],roads_distances[2]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3))))]
            route1_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → Double Shot → Roller Coaster = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Hammer Swing → Fountain → Entrance → Ferris Wheel → Double Shot → Roller Coaster = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["10 7 4 1", "10 7 6 3", "10 7 9 11 8 3"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 2:
            route1 = [roads_distances[9], roads_distances[4]]
            route2 = [roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[1]]
            route3 = [roads_distances[9], roads_distances[6], roads_distances[8], roads_distances[10],roads_distances[7],roads_distances[5], roads_distances[3], roads_distances[1]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3))))]
            route1_asString = f"Hammer Swing → Pirate Ship = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Hammer Swing → Fountain → Entrance → Ferris Wheel → Double Shot → Fountain → {cockfighting_arena} → Pirate Ship = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["10 5", "10 7 4 2", "10 7 9 11 8 6 4 2"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 3:
            route1 = [roads_distances[9], roads_distances[6], roads_distances[5]]
            route2 = [roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0],roads_distances[2]]
            route3 = [roads_distances[9], roads_distances[6], roads_distances[8], roads_distances[10],roads_distances[7]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3))))]
            route1_asString = f"Hammer Swing → Fountain → Double Shot = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster → Double Shot = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Hammer Swing → Fountain → Entrance → Ferris Wheel → Double Shot = {r}{str(routes[2])}m{reset}"
            print(f"{r}\nALL ROUTESs:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["10 7 6", "10 7 4 1 3", "10 7 9 11 8"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 4:
            route1 = [roads_distances[9], roads_distances[6]]
            routes = [eval("+".join(list(map(str, route1))))]
            route1_asString = f"Double Shot → Fountain → Entrance = {r}{str(routes[0])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString]))
            best_route_distance = min(routes)
            print(f"{r}\nBEST ROUTE: {reset}", eval(f"route{routes.index(best_route_distance) + 1}_asString"))
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            return [10,7]
        elif destination == 5:
            print(f"{r}\nALL ROUTES:{reset}\n Hammer Swing = {roads_distances[9]}m")
            print(f"{r}\nBEST ROUTE: {reset}Hammer Swing = {roads_distances[9]}m")
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(roads_distances[9])}m")
            return[10]
        elif destination == 6:
            route1 = [roads_distances[9], roads_distances[6], roads_distances[5], roads_distances[7]]
            route2 = [roads_distances[9], roads_distances[6], roads_distances[8], roads_distances[10]]
            route3 = [roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0],roads_distances[2],roads_distances[7]]
            route4 = [roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0],roads_distances[2],roads_distances[5], roads_distances[8], roads_distances[10]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4))))]
            route1_asString = f"Hammer Swing → Fountain → Double Shot → Ferris Wheel = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → Entrance → Ferris Wheel = {r}{str(routes[1])}m{reset}"
            route3_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Ferris Wheel = {r}{str(routes[2])}m{reset}"
            route4_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Fountain → Entrance → Ferris Wheel = {r}{str(routes[3])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["10 7 6 8", "10 7 9 11", "10 7 4 1 3 8", "10 7 4 1 3 6 9 11", ][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 7:
            route1 = [roads_distances[9], roads_distances[6], roads_distances[8]]
            route2 = [roads_distances[9], roads_distances[6], roads_distances[3], roads_distances[0],roads_distances[2],roads_distances[5], roads_distances[8]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Hammer Swing → Fountain → Entrance = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → {cockfighting_arena} → Roller Coaster → Double Shot → Fountain → Entrance = {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["10 7 9", "10 7 4 1 3 6 9"][
                routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 9:
            route1 = [roads_distances[9], roads_distances[6], roads_distances[3]]
            route2 = [roads_distances[9], roads_distances[6], roads_distances[8], roads_distances[10],roads_distances[7], roads_distances[5], roads_distances[3]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2))))]
            route1_asString = f"Hammer Swing → Fountain → {cockfighting_arena} = {r}{str(routes[0])}m{reset}"
            route2_asString = f"Hammer Swing → Fountain → Entrance → Ferris Wheel → Double Shot → Fountain → {cockfighting_arena}= {r}{str(routes[1])}m{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}\nBEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            return
    elif current_loc == 9:
        if destination == 1:
            route1 = [roads_distances[0]]
            route2 = [roads_distances[3], roads_distances[5], roads_distances[2]]
            route3 = [roads_distances[3], roads_distances[8], roads_distances[10], roads_distances[7],roads_distances[2]]
            route4 = [roads_distances[1], roads_distances[4], roads_distances[6], roads_distances[5], roads_distances[2]]
            route5 = [roads_distances[1], roads_distances[4], roads_distances[6], roads_distances[8], roads_distances[10], roads_distances[7], roads_distances[2]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                        eval("+".join(list(map(str, route5))))]
            route1_asString = f"Roller Coaster = {r}{str(routes[0])}{reset}"
            route2_asString = f"Fountain → Double Shot → Roller Coaster = {r}{str(routes[1])}{reset}"
            route3_asString = f"Fountain → Entrance → Ferris Wheel → Double Shot → Roller Coaster = {r}{str(routes[2])}{reset}"
            route4_asString = f"Pirate Ship → Hammer Swing → Fountain → Double Shot → Roller Coaster = {r}{str(routes[3])}{reset}"
            route5_asString = f"Pirate Ship → Hammer Swing → Fountain → Entrance → Ferris Wheel → Double Shot → Roller Coaster = {r}{str(routes[4])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join(
                [route1_asString, route2_asString, route3_asString, route4_asString, route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["1", "4 6 3", "4 9 11 8 3", "2 5 7 6 3", "2 5 7 9 11 8 3"][
                routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 2:
            route1 = [roads_distances[1]]
            route2 = [roads_distances[3], roads_distances[6], roads_distances[4]]
            route3 = [roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[6], roads_distances[4]]
            route4 = [roads_distances[3], roads_distances[8], roads_distances[11], roads_distances[9], roads_distances[4]]
            route5 = [roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[8], roads_distances[11], roads_distances[9], roads_distances[4]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                        eval("+".join(list(map(str, route5))))]
            route1_asString = f"Pirate Ship = {r}{str(routes[0])}{reset}"
            route2_asString = f"Fountain → Hammer Swing → Pirate Ship = {r}{str(routes[1])}{reset}"
            route3_asString = f"Roller Coaster → Double Shot → Fountain → Hammer Swing → Pirate Ship = {r}{str(routes[2])}{reset}"
            route4_asString = f"Fountain → Entrance → Carousel → Hammer Swing → Pirate Ship = {r}{str(routes[3])}{reset}"
            route5_asString = f"Roller Coaster → Double Shot → Fountain → Entrance → Carousel → Hammer Swing → Pirate Ship = {r}{str(routes[4])}{reset}"
            print(f"{r}\nAll Routes:{reset}\n" + "\n".join(
                [route1_asString, route2_asString, route3_asString, route4_asString, route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}Best route: {reset}", final_bestRoute)
            print(f"{r}Estimated time of arrival:{reset} wala pa")
            roads_to_remove_zombies = ["2", "4 7 5", "1 3 6 7 5", "4 9 12 10 5", "1 3 6 9 12 10 5"][
                routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 3:
            route1 = [roads_distances[3], roads_distances[5]]
            route2 = [roads_distances[0], roads_distances[2]]
            route3 = [roads_distances[1], roads_distances[4], roads_distances[6], roads_distances[5]]
            route4 = [roads_distances[3], roads_distances[8], roads_distances[10], roads_distances[7]]
            route5 = [roads_distances[1], roads_distances[4], roads_distances[6], roads_distances[8],roads_distances[10], roads_distances[7]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                        eval("+".join(list(map(str, route5))))]
            route1_asString = f"Fountain → Double Shot = {r}{str(routes[0])}{reset}"
            route2_asString = f"Roller Coaster → Double Shot = {r}{str(routes[1])}{reset}"
            route3_asString = f"Pirate Ship → Hammer Swing → Fountain → Double Shot = {r}{str(routes[2])}{reset}"
            route4_asString = f"Fountain → Entrance → Ferris Wheel → Double Shot = {r}{str(routes[3])}{reset}"
            route5_asString = f"Pirate Ship → Hammer Swing → Fountain → Entrance → Ferris Wheel → Double Shot = {r}{str(routes[4])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join(
                [route1_asString, route2_asString, route3_asString, route4_asString, route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["4 6", "1 3", "2 5 7 6", "4 9 11 8", "2 5 7 9 11 8"][
                routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 4:
            route1 = [roads_distances[3]]
            route2 = [roads_distances[1], roads_distances[4], roads_distances[6]]
            route3 = [roads_distances[0], roads_distances[2], roads_distances[5]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),
                        eval("+".join(list(map(str, route3))))]
            route1_asString = f"Fountain = {r}{str(routes[0])}{reset}"
            route2_asString = f"Pirate Ship → Hammer Swing → Fountain = {r}{str(routes[1])}{reset}"
            route3_asString = f"Roller Coaster → Double Shot → Fountain = {r}{str(routes[2])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["4", "2 5 7", "1 3 6"][
                routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 5:
            route1 = [roads_distances[1], roads_distances[4]]
            route2 = [roads_distances[3], roads_distances[6]]
            route3 = [roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[6]]
            route4 = [roads_distances[3], roads_distances[8], roads_distances[11], roads_distances[9]]
            route5 = [roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[8], roads_distances[11], roads_distances[9]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),
                        eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                        eval("+".join(list(map(str, route5))))]
            route1_asString = f"Pirate Ship → Hammer Swing = {r}{str(routes[0])}{reset}"
            route2_asString = f"Fountain → Hammer Swing = {r}{str(routes[1])}{reset}"
            route3_asString = f"Roller Coaster → Double Shot → Fountain → Hammer Swing = {r}{str(routes[2])}{reset}"
            route4_asString = f"Fountain → Entrance → Carousel → Hammer Swing = {r}{str(routes[3])}{reset}"
            route5_asString = f"Roller Coaster → Double Shot → Fountain → Entrance → Carousel → Hammer Swing = {r}{str(routes[4])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join(
                [route1_asString, route2_asString, route3_asString, route4_asString, route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["2 5", "4 7", "1 3 6 7", "4 9 12 10", "1 3 6 9 12 10"][
                routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 6:
            route1 = [roads_distances[0], roads_distances[2], roads_distances[7]]
            route2 = [roads_distances[3], roads_distances[5], roads_distances[7]]
            route3 = [roads_distances[1], roads_distances[4], roads_distances[6], roads_distances[5],roads_distances[7]]
            route4 = [roads_distances[1], roads_distances[4], roads_distances[6], roads_distances[8]]
            route5 = [roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[8],roads_distances[10]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),
                        eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                        eval("+".join(list(map(str, route5))))]
            route1_asString = f"Roller Coaster → Double Shot → Ferris Wheel = {r}{str(routes[0])}{reset}"
            route2_asString = f"Fountain → Double Shot → Ferris Wheel = {r}{str(routes[1])}{reset}"
            route3_asString = f"Pirate Ship → Hammer Swing → Fountain → Double Shot → Ferris Wheel = {r}{str(routes[2])}{reset}"
            route4_asString = f"Pirate Ship → Hammer Swing → Fountain → Entrance → Ferris Wheel = {r}{str(routes[3])}{reset}"
            route5_asString = f"Roller Coaster → Double Shot → Fountain → Entrance → Ferris Wheel = {r}{str(routes[4])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join(
                [route1_asString, route2_asString, route3_asString, route4_asString, route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["1 3 8", "4 6 8", "2 5 7 6 8", "2 5 7 9 11", "1 3 6 9 11"][
                routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 7:
            route1 = [roads_distances[3], roads_distances[8]]
            route2 = [roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[8]]
            route3 = [roads_distances[1], roads_distances[4], roads_distances[6], roads_distances[8]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3))))]
            route1_asString = f"Fountain → Entrance = {r}{str(routes[0])}{reset}"
            route2_asString = f"Roller Coaster → Double Shot → Fountain → Entrance = {r}{str(routes[1])}{reset}"
            route3_asString = f"Pirate Ship → Hammer Swing → Fountain → Entrance = {r}{str(routes[2])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["4 9", "1 3 6 9", "2 5 7 9"][
                routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))
        elif destination == 8:
            route1 = [roads_distances[1], roads_distances[4], roads_distances[9]]
            route2 = [roads_distances[3], roads_distances[6], roads_distances[9]]
            route3 = [roads_distances[3], roads_distances[8], roads_distances[11]]
            route4 = [roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[6],roads_distances[9]]
            route5 = [roads_distances[0], roads_distances[2], roads_distances[5], roads_distances[8],roads_distances[11]]
            routes = [eval("+".join(list(map(str, route1)))), eval("+".join(list(map(str, route2)))),eval("+".join(list(map(str, route3)))), eval("+".join(list(map(str, route4)))),
                        eval("+".join(list(map(str, route5))))]
            route1_asString = f"Pirate Ship → Hammer Swing → Carousel = {r}{str(routes[0])}{reset}"
            route2_asString = f"Fountain → Hammer Swing → Carousel = {r}{str(routes[1])}{reset}"
            route3_asString = f"Fountain → Entrance → Carousel = {r}{str(routes[2])}{reset}"
            route4_asString = f"Roller Coaster → Double Shot → Fountain → Hammer Swing → Carousel = {r}{str(routes[3])}{reset}"
            route5_asString = f"Roller Coaster → Double Shot → Fountain → Entrance → Carousel = {r}{str(routes[4])}{reset}"
            print(f"{r}\nALL ROUTES:{reset}\n" + "\n".join([route1_asString, route2_asString, route3_asString, route4_asString, route5_asString]))
            best_route_distance = min(routes)
            final_bestRoute = []
            for i in range(len(routes)):
                if best_route_distance == routes[i]:
                    final_bestRoute.append(eval(f"route{i + 1}_asString"))
            final_bestRoute = min(final_bestRoute)
            print(f"{r}BEST ROUTE: {reset}", final_bestRoute)
            print(f"{r}Estimated Time of Arrival:{reset} {calculate_time(best_route_distance)}")
            roads_to_remove_zombies = ["2 5 10", "4 7 10", "4 9 12", "1 3 6 7 10", "1 3 6 9 12"][routes.index(best_route_distance)]
            return list(map(int, roads_to_remove_zombies.split()))