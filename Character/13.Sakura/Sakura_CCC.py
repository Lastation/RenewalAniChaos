import variable as v;
import func.trig as trg;
import func.trigadv as adv;
import func.trigepic as epic;
import func.sound as s;

function main(playerID)
{
   trg.Debuff_BanReturn();
   trg.Debuff_Stop();

   MoveUnit(All, "40 + 1n Drone", playerID, "Anywhere", "[Skill]HoldPosition");

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] < 16)
         {          
            var d = 360 * v.P_LoopMain[playerID] / 16;
            var n = 4;
            var r = 12 + 12 * v.P_LoopMain[playerID];
            trg.Shape_Circle(playerID, 1, "Protoss Dark Archon", d, n, r);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }
         if (v.P_LoopMain[playerID] == 16)
         {          
            var d = 0;
            var n = 8;
            var r = 200;
            trg.Shape_Circle(playerID, 1, "40 + 1n Mutalisk", d, n, r);
            epic.Shape_Circle(playerID, 1, "40 + 1n Lurker", d, n, r, 0);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Lurker", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 48)
         {                        
            s.CharacterVoice(4);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] < 3)
         {          
            var d = 32 + 32 * v.P_LoopMain[playerID];
            adv.Shape_QuadNxNSquareAt(playerID, 1, "Protoss Dark Archon", 3, 50, d, d);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {          
            var d = 150;
            adv.Shape_QuadNxNSquareAt(playerID, 1, "Protoss Dark Archon", 5, 50, d, d);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 5)
         {          
            var d = 150;
            adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Guardian", 5, 50, d, d);

            trg.Shape_Square(playerID, 1, "40 + 1n Drone", d + 50, d);
            trg.Shape_Square(playerID, 1, "40 + 1n Drone", d - 50, d);
            trg.Shape_Square(playerID, 1, "40 + 1n Drone", d, d + 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Drone", d, d - 50);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Drone", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Drone", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 34)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         if (v.P_LoopMain[playerID] < 3)
         {          
            var d = 50 + 50 * v.P_LoopMain[playerID];
            adv.Shape_QuadNxNSquareAt(playerID, 1, "Protoss Dark Archon", 3, 50, d, 0);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {          
            var d = 200;
            adv.Shape_QuadNxNSquareAt(playerID, 1, "Protoss Dark Archon", 5, 50, d, 0);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 5)
         {          
            var d = 200;
            adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Guardian", 5, 50, d, 0);

            trg.Shape_Square(playerID, 1, "40 + 1n Drone", d + 50, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Drone", d - 50, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Drone", d, 0 + 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Drone", d, 0 - 50);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Drone", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Drone", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 24)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {      
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", playerID);
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
         KillUnitAt(All, "40 + 1n Lurker", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}