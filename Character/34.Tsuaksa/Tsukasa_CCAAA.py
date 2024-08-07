import variable as v;
import func.trig as trg;
import func.trigepic as epic;
import func.sound as s;

var x = 0;
var y = 0;

var d = 0;

function main(playerID)
{
   MoveUnit(All, "60 + 1n Danimoth", playerID, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "40 + 1n Mojo", playerID, "Anywhere", "[Skill]HoldPosition");

   trg.Debuff_BanReturn();
   trg.Debuff_Stop();

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0)
         {          
            trg.Shape_Edge(playerID, 1, "60 + 1n Archon", 0, 3, 120);
            trg.Shape_Edge(playerID, 1, "Kakaru (Twilight)", 0, 3, 120);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1)
         {          
            trg.Shape_Edge(playerID, 1, "60 + 1n Danimoth", 0, 3, 120);
            trg.Shape_Edge(playerID, 1, "100 + 1n Dragoon", 0, 3, 120);
            trg.Shape_Edge(playerID, 1, "60 + 1n Dragoon", 0, 3, 120);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 5)
         {          
            trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", 160, 0);
            trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 64, 0);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 7)
         {          
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 160, 160);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 160, 0);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 9)
         {          
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 120, 120);
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 64, 0);
            trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 64, 0);             
            trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", 120, 120);
            trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", 64, 0);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("60 + 1n High Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);  

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }

         if (v.P_LoopMain[playerID] < 39)
         {
            d = 200;

            trg.Table_Sin(playerID, 15 * v.P_LoopMain[playerID], d);
            trg.Table_Cos(playerID, 15 * v.P_LoopMain[playerID], d);

            x = v.P_AngleCos[playerID];
            y = v.P_AngleSin[playerID];

            trg.Shape_Square(playerID, 1, "60 + 1n Archon", x, y);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);


            if (v.P_LoopMain[playerID] >= 17 && v.P_LoopMain[playerID] % 2 == 0)
            {
               trg.Shape_Square(playerID, 1, "60 + 1n Siege", x, y);
            }
         }
         else if (v.P_LoopMain[playerID] < 69)
         {
            d = 100;

            trg.Table_Sin(playerID, 15 * v.P_LoopMain[playerID], d);
            trg.Table_Cos(playerID, 15 * v.P_LoopMain[playerID], d);

            x = v.P_AngleCos[playerID];
            y = v.P_AngleSin[playerID];

            trg.Shape_Square(playerID, 1, "Protoss Dark Templar", x, y);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", playerID);
         }
         if (v.P_LoopMain[playerID] == 70)
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID);

            CreateUnit(16, "60 + 1n Siege", dwrand() % 8 + 33, playerID);
            SetInvincibility(Enable, "60 + 1n Siege", playerID, "Anywhere");
         }

         if (v.P_LoopMain[playerID] == 39)
         {
            s.CharacterVoice(6);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 75)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill")
         && v.P_Step[playerID] == 240)
         {
            s.CharacterVoice(7);
            v.P_SkillDelay[playerID] = 0;
            v.P_CountMain[playerID] = 0;
            v.P_LoopMain[playerID] = 0;
            v.P_Step[playerID] = 250;
            KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID);
         }
         else 
         {
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
            trg.SkillEnd();
         }
      }
   }
}