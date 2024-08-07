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
         RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 3)
         {          
            var d = 0;
            var n = 8;
            var r = 50 + 50 * v.P_LoopMain[playerID];
            trg.Shape_Circle(playerID, 1, "Protoss Dark Archon", d, n, r);
            trg.Shape_Circle(playerID, 1, "40 + 1n Mutalisk", d, n, r);
            epic.Shape_Circle(playerID, 1, "40 + 1n Lurker", d, n, r, 2);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Lurker", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3)
         {          
            var d = 0;
            var n = 8;
            var r = 50 + 50 * v.P_LoopMain[playerID];
            trg.Shape_Circle(playerID, 1, "Protoss Dark Archon", d, n, r);
            trg.Shape_Circle(playerID, 1, "40 + 1n Mutalisk", d, n, r);
            epic.Shape_Circle(playerID, 1, "40 + 1n Lurker", d, n, r, 0);

            CreateUnitWithProperties(1, "40 + 1n Lurker", "[Skill]Hallu_Bozo", playerID, UnitProperty(burrowed = true));

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Lurker", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }
         
         if (v.P_LoopMain[playerID] > 3)
         {
            if (v.P_LoopMain[playerID] % 4 == 0)
            {
               var d = 0;
               var n = 8;
               var r = 200;
               trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", d, n, r);

               MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
               Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            }
            else if (v.P_LoopMain[playerID] % 4 == 1)
            {
               for (var i = 0; i < 8; i++)
               {
                  adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 40, 0);
                  adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 32, 32);

                  RemoveUnitAt(1, "40 + 1n Guardian", "Anywhere", playerID);
               }

               KillUnitAt(All, "80 + 1n Guardian", "Anywhere", playerID);
            }
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 48)
         {                        
            s.CharacterVoice(6);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] % 4 == 0)
         {
            var d = 0;
            var n = 8;
            var r = 200;
            trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", d, n, r);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         else if (v.P_LoopMain[playerID] % 4 == 1)
         {
            for (var i = 0; i < 8; i++)
            {
               adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 40, 0);
               adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 32, 32);

               RemoveUnitAt(1, "40 + 1n Guardian", "Anywhere", playerID);
            }

            KillUnitAt(All, "80 + 1n Guardian", "Anywhere", playerID);
         }

         if (Bring(playerID, AtLeast, 1, "40 + 1n Lurker", "Anywhere"))
         {
            for (var i = 0; i < 2; i++)
            {
               adv.Shape_SquareAt(playerID, "40 + 1n Lurker", 1, "80 + 1n Guardian", 16, 16);
               adv.Shape_SquareAt(playerID, "40 + 1n Lurker", 1, "Protoss Dark Archon", 16, 16);

               trg.MoveLoc("40 + 1n Lurker", playerID, 0, 0);
               RemoveUnitAt(1, "40 + 1n Lurker", "Anywhere", playerID);
               trg.SkillUnit(playerID, 1, "40 + 1n Drone");
            }

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "80 + 1n Guardian", "Anywhere", playerID);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 36)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {      
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", playerID);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}