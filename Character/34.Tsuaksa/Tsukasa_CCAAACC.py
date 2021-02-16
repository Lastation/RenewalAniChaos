import variable as v;
import func.trig as trg;
import func.trigepic as epic;

var x = 0;
var y = 0;

var d = 0;

function Move_Square(playerID : TrgPlayer, count, unit : TrgUnit, pos_x, pos_y);

function main(playerID)
{
   MoveUnit(All, "60 + 1n High Templar", playerID, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "60 + 1n Dragoon", playerID, "Anywhere", "[Skill]HoldPosition");

   trg.Debuff_BanReturn();
   trg.Debuff_Stop();

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0)
         {          
            trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", 32, 32);
            trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", 160, 0);
            trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", 224, 64);
            trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", 224, -64);
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 32, 32);
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 160, 0);
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 224, 64);
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 224, -64);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 64, 0);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 96, 96);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 160, 96);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 96, 160);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);

         }
         else if (v.P_LoopMain[playerID] == 1)
         {
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 64, 64);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
            Move_Square(playerID, 1, "60 + 1n Siege", 64, 64);
         }
         else if (v.P_LoopMain[playerID] == 2)
         {          
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 64, 0);
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 96, 96);
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 160, 96);
            trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 96, 160);
            trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", 64, 0);
            trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", 96, 96);
            trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", 160, 96);
            trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", 96, 160);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 32, 32);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 160, 0);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 224, 64);
            trg.Shape_Square(playerID, 1, "60 + 1n Archon", 224, -64);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3)
         {
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 256, 0);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 224, 64);
            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 224, -64);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
            Move_Square(playerID, 1, "60 + 1n Siege", 256, 0);
            Move_Square(playerID, 1, "60 + 1n Siege", 224, 64);
            Move_Square(playerID, 1, "60 + 1n Siege", 224, -64);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 11)
         {          
            epic.Shape_Square(playerID, 1, "60 + 1n Danimoth", 96, 0, 1);
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 96, 0);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 12)
         {          
            epic.Shape_Square(playerID, 1, "60 + 1n Danimoth", 64, 128, 1);
            trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 64, 128);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("60 + 1n High Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }         
         else if (v.P_LoopMain[playerID] == 13)
         {          
            epic.Shape_Square(playerID, 1, "60 + 1n Danimoth", 128, 64, 1);
            trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 128, 64);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("60 + 1n High Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }         
         else if (v.P_LoopMain[playerID] == 14)
         {          
            epic.Shape_Square(playerID, 1, "60 + 1n Danimoth", 160, 0, 1);
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 160, 0);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 15)
         {          
            epic.Shape_Square(playerID, 1, "60 + 1n Danimoth", 160, 96, 1);
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 160, 96);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 16)
         {          
            epic.Shape_Square(playerID, 1, "60 + 1n Danimoth", 96, 160, 1);
            trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 96, 160);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         }

         if (v.P_LoopMain[playerID] > 14)
         {
            if (v.P_LoopMain[playerID] % 2 == 0)
            {
               d = 100;

               trg.Table_Sin(playerID, 30 * v.P_LoopMain[playerID], d);
               trg.Table_Cos(playerID, 30 * v.P_LoopMain[playerID], d);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               trg.Shape_Square(playerID, 1, "Protoss Dark Templar", x, y);
               KillUnitAt(All, "Protoss Dark Templar", "Anywhere", playerID);
            }
            else
            {
               d = 200;

               trg.Table_Sin(playerID, 30 * v.P_LoopMain[playerID], d);
               trg.Table_Cos(playerID, 30 * v.P_LoopMain[playerID], d);

               x = v.P_AngleCos[playerID];
               y = v.P_AngleSin[playerID];

               trg.Shape_Square(playerID, 1, " Unit. Schnee", x, y);
               KillUnitAt(All, " Unit. Schnee", "Anywhere", playerID);
            }
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 35)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
         
         trg.SkillEnd();
      }
   }
}

function Move_Square(playerID : TrgPlayer, count, unit : TrgUnit, pos_x, pos_y)
{
   if (pos_x == 0 && pos_y == 0)
   {
      trg.Shape_Dot(playerID, count, unit, pos_x, pos_y);
   }
   else
   {
      trg.MoveLoc(v.P_UnitID[playerID], playerID, pos_x, pos_y);
      MoveUnit(count, unit, playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
      trg.MoveLoc(v.P_UnitID[playerID], playerID, -pos_y, pos_x);
      MoveUnit(count, unit, playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
      trg.MoveLoc(v.P_UnitID[playerID], playerID, -pos_x, -pos_y);
      MoveUnit(count, unit, playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
      trg.MoveLoc(v.P_UnitID[playerID], playerID, pos_y, -pos_x);
      MoveUnit(count, unit, playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
   }
}